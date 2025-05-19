# HookGuard

**HookGuard** is a lightweight FastAPI tool that catches incoming webhooks, forwards them to your real endpoint, retries failed deliveries automatically, and logs results.

## 🔧 Features
- `/catch` endpoint for webhooks
- Forwards to real destination (`FORWARD_URL`)
- Retries on failure with backoff
- Logs all attempts in SQLite
- `/logs` endpoint to review past requests

## ⚙️ Setup

```bash
git clone https://github.com/yourusername/hookguard.git
cd hookguard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` with your actual destination URL, then run:

```bash
uvicorn app.main:app --reload
```

## 💡 .env.example
```
FORWARD_URL=https://webhook.site/your-url
MAX_RETRIES=3
RETRY_DELAY=5
```

## 📦 Coming Soon
- Hosted version
- Slack/email alerts
- Usage limits + billing
- Web UI dashboard
