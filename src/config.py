import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
CHAT_ID = os.getenv("CHAT_ID")
ALLOWED_USER = [int(id) for id in CHAT_ID.split(",")]

DB_PATH = os.getenv("DB_PATH", str(BASE_DIR / 'falconbot.db'))
SCREENSHOT_DIR = os.getenv("SCREENSHOT_PATH", "/tmp")

NETSPY_PATH = os.getenv("NETSPY_PATH")
if not NETSPY_PATH:
    raise ValueError("NETSPY_PATH is not set in the .env file")