import sqlite3
from datetime import datetime

DB = "decisions.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS decisions (
        station_id TEXT,
        driver_token TEXT,
        status TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_decision(station_id, token, status):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "INSERT INTO decisions VALUES (?, ?, ?, ?)",
        (station_id, token, status, datetime.utcnow().isoformat())
    )

    conn.commit()
    conn.close()