import os
import time
import logging
from src.config import ALLOWED_USER, SECRET_PIN

# Session tracking
pin_sessions = {}   # chat_id -> expiry timestamp
pin_attempts = {}   # chat_id -> failed attempts

LOCKOUT_TIME = 600
SESSION_TIME = 300
MAX_ATTEMPTS = 3

def is_allowed(bot, message):
    if message.chat.id not in ALLOWED_USER:
        bot.reply_to(message, "Unauthorized access.")
        logging.warning(f"Unauthorized access attempt from {message.chat.id} - @{message.from_user.username}")
        return False
    return True

def is_locked_out(chat_id):
    if chat_id in pin_attempts:
        attempts, lockout_until = pin_attempts[chat_id]
        if attempts >= MAX_ATTEMPTS and time.time() < lockout_until:
            return True
    return False

def has_vaild_session(chat_id):
    if chat_id in pin_sessions:
        if time.time() < pin_sessions[chat_id]:
            return True
    return False

def verify_pin(chat_id, entered_pin):
    if is_locked_out(chat_id):
        return "locked"
    
    if entered_pin == SECRET_PIN:
        pin_sessions[chat_id] = time.time() + SESSION_TIME
        pin_attempts[chat_id] = (0,0)   #reset attempts
        return "success"
    else:
        attempts = pin_attempts.get(chat_id, (0,0))[0] + 1
        lockout_util = time.time() + LOCKOUT_TIME if attempts >= MAX_ATTEMPTS else 0
        pin_attempts[chat_id] = (attempts, lockout_util)
        remaining = MAX_ATTEMPTS - attempts
        return f"Failed:{remaining} attempts left"