import os
import logging

ALLOWED_USER = [int(os.getenv("ADMIN_ID"))]

def is_allowed(bot, message):
    if message.chat.id not in ALLOWED_USER:
        bot.reply_to(message, "Unauthorized access.")
        logging.warning(f"Unauthorized access attempt from {message.chat.id} - @{message.from_user.username}")
        return False
    return True
