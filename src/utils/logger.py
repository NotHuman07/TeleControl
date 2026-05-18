import sqlite3
import logging
from datetime import datetime
from src.config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            username TEXT,
            command TEXT,
            chat_id INTEGER)''')

    conn.commit()
    conn.close()

def log_command(message):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO logs (timestamp, username, command, chat_id) VALUES (?, ?, ?, ?)",
                    (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                    message.from_user.username or "unknown",
                    message.text,
                    message.chat.id
                    )
        )
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f"Failed to log command: {e}")