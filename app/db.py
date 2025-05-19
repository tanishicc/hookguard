import sqlite3
import json
import os

DB_FILE = os.path.join(os.path.dirname(__file__), "..", "webhook_logs.db")

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS webhooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            payload TEXT,
            headers TEXT,
            timestamp TEXT,
            status TEXT,
            retries INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def log_status(payload, headers, status, retries):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO webhooks (payload, headers, timestamp, status, retries)
        VALUES (?, ?, datetime('now'), ?, ?)
    ''', (json.dumps(payload), json.dumps(headers), status, retries))
    conn.commit()
    conn.close()

def get_recent_logs(limit=100):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM webhooks ORDER BY id DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

init_db()
