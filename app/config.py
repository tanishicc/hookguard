import os
from dotenv import load_dotenv

load_dotenv()

FORWARD_URL = os.getenv("FORWARD_URL", "https://example.com/webhook")
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", 5))
