import telebot
import threading
import os
import platform
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

CHAT_ID = os.getenv("CHAT_ID")

from src.handlers import resgister_handlers
from src.network import watch_network

resgister_handlers(bot)

thread = threading.Thread(target=watch_network, args=(bot, CHAT_ID))
thread.daemon = True

thread.start()
bot.polling()
