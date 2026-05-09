from __future__ import annotations

from .memory import default_memory


def main() -> None:
    mem = default_memory()

    mem.upsert_contact(
        name="Owner Representative",
        email="owner.rep@example.com",
        role="Owner Rep",
        company="Client Co.",
        culture_region="high_context",
        preferred_tone="formal",
        notes="Prefers concise but respectful updates.",
    )
    mem.upsert_contact(
        name="Structural Engineer",
        email="struct.eng@example.com",
        role="Structural Engineer",
        company="ACME Consulting",
        culture_region="low_context",
        preferred_tone="direct",
        notes="Prefers clear action items and dates.",
    )
    mem.upsert_contact(
        name="Subcontractor PM",
        email="sub.pm@example.com",
        role="Subcontractor PM",
        company="SteelWorks Ltd.",
        culture_region="mixed",
        preferred_tone="friendly",
        notes="Responds well to collaborative tone.",
    )

    print("Seeded contacts into memory.db")


if __name__ == "__main__":
    main()
