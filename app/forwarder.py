import httpx
import time
from app.db import log_status
from app.config import FORWARD_URL, MAX_RETRIES, RETRY_DELAY

def forward_webhook(payload, headers, retries=0):
    try:
        print(f"Forwarding to {FORWARD_URL} (Attempt {retries + 1})")
        safe_headers = {k: v for k, v in headers.items() if k.lower() != "content-length"}
        response = httpx.post(FORWARD_URL, json=payload, headers=safe_headers, timeout=10)
        print(f"Response: {response.status_code}, Body: {response.text}")

        if 200 <= response.status_code < 300:
            print("✅ Success!")
            log_status(payload, headers, "success", retries)
        else:
            raise Exception(f"❌ Failed with status code: {response.status_code}")

    except Exception as e:
        print(f"⚠️ Error forwarding webhook: {e}")
        if retries < MAX_RETRIES:
            time.sleep(RETRY_DELAY * (retries + 1))
            forward_webhook(payload, headers, retries + 1)
        else:
            print("❌ Max retries reached — logging as failed.")
            log_status(payload, headers, "failed", retries)
