"""Read and create calendar events on the same Gmail account used for mail triage (CalDAV)."""

from __future__ import annotations

import re
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from typing import Any
from urllib.parse import quote

import httpx

from demo.reader import EMAIL_ADDRESS, EMAIL_PASSWORD

_CALENDAR_QUERY = """<?xml version="1.0" encoding="utf-8" ?>
<C:calendar-query xmlns:D="DAV:" xmlns:C="urn:ietf:params:xml:ns:caldav">
  <D:prop>
    <D:getetag/>
    <C:calendar-data/>
  </D:prop>
  <C:filter>
    <C:comp-filter name="VCALENDAR">
      <C:comp-filter name="VEVENT">
        <C:time-range start="{start}" end="{end}"/>
      </C:comp-filter>
    </C:comp-filter>
  </C:filter>
</C:calendar-query>"""


def _require_credentials() -> None:
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        raise RuntimeError(
            "EMAIL_ADDRESS and EMAIL_PASSWORD must be set in project/.env "
            "(same mailbox as Inbox / mail triage)"
        )


def _caldav_event_urls(email: str) -> list[str]:
    encoded = quote(email, safe="")
    return [
        f"https://apidata.googleusercontent.com/caldav/v2/{encoded}/events/",
        f"https://calendar.google.com/calendar/dav/{encoded}/events/",
    ]


def _unfold_ical(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    for line in lines:
        if line.startswith((" ", "\t")) and out:
            out[-1] += line[1:]
        else:
            out.append(line)
    return "\n".join(out)


def _ical_escape(text: str) -> str:
    return (
        text.replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


def _format_ical_datetime(dt: datetime, *, all_day: bool) -> str:
    if all_day:
        return dt.astimezone(timezone.utc).strftime("%Y%m%d")
    return dt.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _parse_event_datetime(value: str, *, all_day: bool) -> datetime:
    raw = (value or "").strip()
    if not raw:
        raise ValueError("Date/time is required")
    if all_day:
        return datetime.strptime(raw[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    if raw.endswith("Z"):
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(timezone.utc)
    dt = datetime.fromisoformat(raw)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _parse_attendees(block: str) -> list[str]:
    attendees: list[str] = []
    for line in block.splitlines():
        if not line.startswith("ATTENDEE"):
            continue
        match = re.search(r":(?:mailto:)?([^;\s]+)", line, re.IGNORECASE)
        if match:
            attendees.append(match.group(1).strip().lower())
    return attendees


def _ical_prop(block: str, name: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(name)}(?:;[^:]*)?:(.*)$", re.MULTILINE)
    match = pattern.search(block)
    if not match:
        return None
    return match.group(1).strip()


def _parse_ical_datetime(value: str) -> datetime | None:
    value = (value or "").strip()
    if not value:
        return None
    if value.endswith("Z"):
        for fmt in ("%Y%m%dT%H%M%SZ", "%Y%m%dT%H%M.%fZ"):
            try:
                return datetime.strptime(value, fmt).replace(tzinfo=timezone.utc)
            except ValueError:
                continue
    if "T" in value:
        core = value.split("T", 1)[0] + "T" + value.split("T", 1)[1][:6]
        try:
            return datetime.strptime(core, "%Y%m%dT%H%M%S").replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    if len(value) >= 8 and value[:8].isdigit():
        try:
            return datetime.strptime(value[:8], "%Y%m%d").replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    return None


def _parse_vevents(ical_text: str) -> list[dict]:
    text = _unfold_ical(ical_text)
    events: list[dict] = []
    for part in text.split("BEGIN:VEVENT"):
        if "END:VEVENT" not in part:
            continue
        block = part.split("END:VEVENT", 1)[0]
        dtstart_raw = _ical_prop(block, "DTSTART")
        start = _parse_ical_datetime(dtstart_raw or "")
        if not start:
            continue
        dtend_raw = _ical_prop(block, "DTEND")
        end = _parse_ical_datetime(dtend_raw or "") if dtend_raw else None
        events.append(
            {
                "uid": _ical_prop(block, "UID"),
                "title": _ical_prop(block, "SUMMARY") or "(No title)",
                "location": _ical_prop(block, "LOCATION"),
                "description": _ical_prop(block, "DESCRIPTION"),
                "start": start.isoformat(),
                "end": end.isoformat() if end else None,
                "all_day": bool(dtstart_raw and "T" not in dtstart_raw),
                "attendees": _parse_attendees(block),
            }
        )
    return events


def _extract_calendar_data(xml_text: str) -> list[str]:
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []
    tag = "{urn:ietf:params:xml:ns:caldav}calendar-data"
    return [el.text for el in root.iter(tag) if el.text]


def _caldav_report(url: str, start_str: str, end_str: str) -> str:
    body = _CALENDAR_QUERY.format(start=start_str, end=end_str)
    with httpx.Client(timeout=30.0, follow_redirects=True) as client:
        resp = client.request(
            "REPORT",
            url,
            content=body,
            auth=(EMAIL_ADDRESS, EMAIL_PASSWORD),
            headers={
                "Depth": "1",
                "Content-Type": "application/xml; charset=utf-8",
            },
        )
        resp.raise_for_status()
        return resp.text


def _fetch_calendar_events(*, days: int, limit: int) -> list[dict[str, Any]]:
    _require_credentials()
    days = max(1, min(days, 60))
    limit = max(1, min(limit, 100))

    now = datetime.now(timezone.utc)
    end = now + timedelta(days=days)
    start_str = now.strftime("%Y%m%dT%H%M%SZ")
    end_str = end.strftime("%Y%m%dT%H%M%SZ")

    last_error: Exception | None = None
    parsed: list[dict[str, Any]] = []
    saw_response = False
    for url in _caldav_event_urls(EMAIL_ADDRESS):
        try:
            xml_text = _caldav_report(url, start_str, end_str)
            saw_response = True
            for ical in _extract_calendar_data(xml_text):
                parsed.extend(_parse_vevents(ical))
            break
        except Exception as exc:
            last_error = exc
            continue

    if not saw_response and last_error is not None:
        raise RuntimeError(
            "Could not load Google Calendar for the triage mailbox via CalDAV. "
            "Same EMAIL_ADDRESS / app password as Inbox; ensure Calendar sync is enabled. "
            f"({last_error})"
        ) from last_error

    parsed.sort(key=lambda item: item["start"])
    return parsed[:limit]


def _build_vevent_ical(
    *,
    uid: str,
    title: str,
    start: datetime,
    end: datetime,
    all_day: bool,
    location: str | None,
    description: str | None,
    attendees: list[str],
) -> str:
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//CEM501 Demo Agent//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:REQUEST",
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{now}",
        f"SUMMARY:{_ical_escape(title)}",
        f"ORGANIZER;CN={_ical_escape(EMAIL_ADDRESS)}:mailto:{EMAIL_ADDRESS}",
    ]
    if all_day:
        lines.append(f"DTSTART;VALUE=DATE:{_format_ical_datetime(start, all_day=True)}")
        lines.append(f"DTEND;VALUE=DATE:{_format_ical_datetime(end, all_day=True)}")
    else:
        lines.append(f"DTSTART:{_format_ical_datetime(start, all_day=False)}")
        lines.append(f"DTEND:{_format_ical_datetime(end, all_day=False)}")
    if location:
        lines.append(f"LOCATION:{_ical_escape(location)}")
    if description:
        lines.append(f"DESCRIPTION:{_ical_escape(description)}")
    for attendee in attendees:
        email = attendee.strip().lower()
        if not email or "@" not in email:
            continue
        lines.append(
            "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;"
            f"PARTSTAT=NEEDS-ACTION;RSVP=TRUE:mailto:{email}"
        )
    lines.extend(["END:VEVENT", "END:VCALENDAR"])
    return "\r\n".join(lines) + "\r\n"


def _caldav_put_event(base_url: str, uid: str, ical_body: str) -> None:
    resource = quote(f"{uid}.ics", safe="")
    url = base_url if base_url.endswith("/") else base_url + "/"
    url += resource
    with httpx.Client(timeout=30.0, follow_redirects=True) as client:
        resp = client.put(
            url,
            content=ical_body,
            auth=(EMAIL_ADDRESS, EMAIL_PASSWORD),
            headers={"Content-Type": "text/calendar; charset=utf-8"},
        )
        if resp.status_code not in (200, 201, 204):
            resp.raise_for_status()


def create_calendar_event(
    *,
    title: str,
    start: str,
    end: str | None = None,
    all_day: bool = False,
    location: str | None = None,
    description: str | None = None,
    attendees: list[str] | None = None,
) -> dict[str, Any]:
    """Create a calendar event (and send invites when attendees are provided)."""
    _require_credentials()
    title = (title or "").strip()
    if not title:
        raise ValueError("Title is required")

    start_dt = _parse_event_datetime(start, all_day=all_day)
    if end:
        end_dt = _parse_event_datetime(end, all_day=all_day)
    elif all_day:
        end_dt = start_dt + timedelta(days=1)
    else:
        end_dt = start_dt + timedelta(hours=1)

    if all_day and end_dt <= start_dt:
        end_dt = start_dt + timedelta(days=1)
    elif not all_day and end_dt <= start_dt:
        raise ValueError("End time must be after start time")

    clean_attendees: list[str] = []
    for raw in attendees or []:
        for part in re.split(r"[,;\s]+", raw):
            email = part.strip().lower()
            if email and "@" in email:
                clean_attendees.append(email)

    uid = f"{uuid.uuid4()}@cem501.demo"
    ical_body = _build_vevent_ical(
        uid=uid,
        title=title,
        start=start_dt,
        end=end_dt,
        all_day=all_day,
        location=(location or "").strip() or None,
        description=(description or "").strip() or None,
        attendees=clean_attendees,
    )

    last_error: Exception | None = None
    for base_url in _caldav_event_urls(EMAIL_ADDRESS):
        try:
            _caldav_put_event(base_url, uid, ical_body)
            return {
                "uid": uid,
                "title": title,
                "start": start_dt.isoformat(),
                "end": end_dt.isoformat(),
                "all_day": all_day,
                "location": (location or "").strip() or None,
                "description": (description or "").strip() or None,
                "attendees": clean_attendees,
            }
        except Exception as exc:
            last_error = exc
            continue

    raise RuntimeError(
        "Could not create calendar event on the triage mailbox. "
        f"({last_error})"
    ) from last_error


def read_upcoming_calendar_events(*, days: int = 7, limit: int = 15) -> list[dict[str, Any]]:
    """Return upcoming primary-calendar events for the triage mailbox (EMAIL_ADDRESS)."""
    return _fetch_calendar_events(days=days, limit=limit)
