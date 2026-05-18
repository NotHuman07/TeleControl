import telebot
import threading
import os
import platform
from dotenv import load_dotenv
from src.utils.logger import init_db
from src.config import BOT_TOKEN, ADMIN_ID
init_db()

bot = telebot.TeleBot(BOT_TOKEN)

from src.handlers import register_handlers
from src.services.network import watch_network

register_handlers(bot)

thread = threading.Thread(target=watch_network, args=(bot, ADMIN_ID))
thread.daemon = True

thread.start()
bot.polling()
