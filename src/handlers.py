import logging
import time
import os
from src.utils.auth import is_allowed, verify_pin, has_vaild_session, is_locked_out
from src.services import system
from src.config import DB_PATH
from src.utils.logger import log_command
import sqlite3

# Trace who is waiting to entre PIN and for what cmd
waiting_for_pin = {} #chat_id -> screenshot/shell


def register_handlers(bot):

    @bot.message_handler(commands=['start'])
    def start(message):

        if not is_allowed(bot, message): return
        bot.reply_to(message, "Alert system active! I'll notify you when new device join.")
        

    @bot.message_handler(commands=['wifi'])
    def who_is_on_wifi(message):
        if not is_allowed(bot, message): return
        log_command(message)
        try:
            bot.reply_to (message, system.who_is_on_wifi())
        except Exception as e:
            bot.reply_to(message, f"wifi error: {str(e)}")

    @bot.message_handler(commands=['cpu'])
    def cpu_usage(message):
        if not is_allowed(bot, message): return
        log_command(message)
        try:
            bot.reply_to(message, system.cpu_usage())
        except Exception as e:
            bot.reply_to(message, f"cpu error: {str(e)}")

    @bot.message_handler(commands=['disk'])
    def disk_usage(message):
        if not is_allowed(bot, message): return
        log_command(message)
        try:
            bot.reply_to(message, system.disk_usage())
        except Exception as e:
            bot.reply_to(message, f"disk error: {str(e)}")

    @bot.message_handler(commands=['temp'])
    def temp(message):
        if not is_allowed(bot, message): return
        log_command(message)
        try:
            bot.reply_to(message, system.temp())
        except Exception as e:
            bot.reply_to(message, f"temp error: {str(e)}")
    
    @bot.message_handler(commands=['screenshot'])
    def screenshot(message):
        if not is_allowed(bot, message): return
        log_command(message)

        if is_locked_out(message.chat.id):
            bot.reply_to(message, "Too many wrong PIN attempts. Try again in 10 minutes." )
            return
        if has_vaild_session(message.chat.id):
            _take_screenshot(bot, message)
            return
        waiting_for_pin[message.chat.id] = 'screenshot'
        bot.reply_to(message, "Enter your PIN:")
        
    
    @bot.message_handler(commands=['shell'])
    def shell(message):
        if not is_allowed(bot, message): return
        log_command(message)

        if is_locked_out(message.chat.id):
            bot.reply_to(message, "Too many wrong PIN attempts. Try again in 10 minutes." )
            return
        
        parts = message.text.split(' ', 1)
        if len(parts) < 2:
            bot.reply_to(message, "Usage: /shell <command>\nExample: /shell ls -la")
            return
        if has_vaild_session(message.chat.id):
            bot.reply_to(message, system.shell(parts[1]))
            return
        
        waiting_for_pin[message.chat.id] = f'shell:{parts[1]}'
        bot.reply_to(message, "Enter your PIN:")

    def _take_screenshot(bot, message):
            try:
                filename = system.screenshot()
                with open (filename, 'rb') as photo:
                    sent = bot.send_photo(message.chat.id, photo)
            except Exception as e:
                bot.reply_to(message, f"screenshot error: {str(e)}")

    @bot.message_handler(func=lambda message: message.chat.id in waiting_for_pin)
    def handle_pin(message):
        if not is_allowed(bot,message):
            return
        chat_id = message.chat.id
        
        try:
            bot.delete_message(chat_id, message.message_id)
        except Exception as e:
            logging.warning(f"Could not delete message: {e}")

        result = verify_pin(chat_id, message.text.strip())

        if result == "success":
            action = waiting_for_pin.pop(chat_id)
            bot.send_message(chat_id, "PIN correct. Session vaild for 5 minutes.")
            if action == 'screenshot':
                _take_screenshot(bot, message)
            elif action.startswith('shell:'):
                cmd = action.split(':', 1)[1]
                bot.reply_to(message, system.run_shell(cmd))
        elif result == "locked":
            waiting_for_pin.pop(chat_id)
            bot.send_message(chat_id, "Bye-bye! Locked out for 10 minutes.")
        else:
            remaining = result.split(':')[1]
            bot.send_message(chat_id, f"Wrong PIN. {remaining} attempts left.")

        


    @bot.message_handler(commands=['logs'])
    def logs(message):
        if not is_allowed(bot, message): return
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("SELECT timestamp, username, command FROM logs ORDER BY id DESC LIMIT 10")

            rows = c.fetchall()
            conn.close()
            if not rows:
                bot.reply_to(message, "No logs yet.")
                return
            output = "last 10 commands:\n\n"
            for row in rows:
                output += f"🕐{row[0]}\n👤 @{row[1]}\n⚡ {row[2]}\n\n"
            bot.reply_to(message, output)
        except Exception as e:
            bot.reply_to(message, f"❌logs error: {str(e)}")
