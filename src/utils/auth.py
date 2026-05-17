import os

ALLOWED_USER = [int(os.getenv("CHAT_ID"))]

def is_allowed(message):
    if message.chat.id not in ALLOWED_USER:
        bot.reply_to(message, "Unauthorized access.")
        print(f"Unauthorized access attempt from {message.chat.id} - @{message.from_user.username}")
        return False
    return True
