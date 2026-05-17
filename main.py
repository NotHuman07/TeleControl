import telebot
import threading
import os
import platform
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

CHAT_ID = (int(chat_id) for chat_id in os.getenv("CHAT_ID").split(","))

from src.handlers import register_handlers
from src.services.network import watch_network

register_handlers(bot)

thread = threading.Thread(target=watch_network, args=(bot, CHAT_ID))
thread.daemon = True

thread.start()
bot.polling()
