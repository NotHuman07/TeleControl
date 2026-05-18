import telebot
import threading
import os
import platform
from dotenv import load_dotenv
from src.utils.logger import init_db

init_db()

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

ADMIN_ID = int(os.getenv("ADMIN_ID"))
from src.handlers import register_handlers
from src.services.network import watch_network

register_handlers(bot)

thread = threading.Thread(target=watch_network, args=(bot, ADMIN_ID))
thread.daemon = True

thread.start()
bot.polling()
