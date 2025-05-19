from fastapi import FastAPI, Request, BackgroundTasks
from app.forwarder import forward_webhook
from app.db import get_recent_logs

app = FastAPI()

@app.post("/catch")
async def catch_webhook(request: Request, background_tasks: BackgroundTasks):
    headers = dict(request.headers)
    payload = await request.json()
    background_tasks.add_task(forward_webhook, payload, headers)
    return {"status": "received"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/logs")
def get_logs():
    return {"logs": get_recent_logs()}
