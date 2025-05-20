from fastapi import FastAPI, Request, BackgroundTasks
from app.forwarder import forward_webhook
from app.db import get_recent_logs

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to HookGuard 👋"}

@app.post("/catch")
async def catch_webhook(request: Request, background_tasks: BackgroundTasks):
    headers = dict(request.headers)
    content_type = headers.get("content-type", "")

    if "application/json" in content_type:
        data = await request.json()
    else:
        form = await request.form()
        data = dict(form)

    forward_url = data.get("forward_url")
    if not forward_url:
        return {"error": "Missing forward_url"}

    background_tasks.add_task(forward_webhook, data, headers, forward_url)
    return {"status": "received"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/logs")
def get_logs():
    return {"logs": get_recent_logs()}
