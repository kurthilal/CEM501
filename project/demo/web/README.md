# Demo web dashboard

Flask UI that wraps the same Python modules as the rest of `demo/`:

- **Classifier** — `/api/classify`
- **Drafter** — `/api/draft`
- **Pipeline** — `/api/pipeline`
- **Inbox** — `/api/inbox` → `demo.reader.read_recent_emails`
- **Memory** — `/api/memory/*` → `demo/memory/memory.db`
- **SMTP** — `/api/send` (only if `WEB_ALLOW_SEND=1`)

## Run

From **`project/`**:

```bash
pip install -r requirements.txt
python3 -m demo.web.app
```

Open **http://127.0.0.1:5000**

Do not expose this app on a public network without authentication and HTTPS.
