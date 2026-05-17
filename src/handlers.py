from src.utils.auth import is_allowed
from src.services import system

def resgister_handlers(bot):

    @bot.message_handler(commands=['start'])
    def start(message):

        if not is_allowed(bot, message): return
        bot.reply_to(message, "Alert system active! I'll notify you when new device join.")
        

    @bot.message_handler(commands=['wifi'])
    def who_is_on_wifi(message):
        if not is_allowed(bot, message): return
        try:
            bot.reply_to (message, system.who_is_on_wifi())
        except Exception as e:
            bot.reply_to(message, f"wifi error: {str(e)}")

    @bot.message_handler(commands=['cpu'])
    def cpu_usage(message):
        if not is_allowed(bot, message): return
        try:
            bot.reply_to(message, system.cpu_usage())

    @bot.message_handler(commands=['disk'])
    def disk_usage(message):
        if not is_allowed(bot, message): return
        try:
            bot.reply_to(message, system.disk_usage())
        except Exception as e:
            bot.reply_to(message, f"disk error: {str(e)}")

    @bot.message_handler(commands=['temp'])
    def temp(message):
        if not is_allowed(bot, message): return
        try:
            bot.reply_to(message, system.temp())
        except Exception as e:
            bot.reply_to(message, f"temp error: {str(e)}")
    
    @bot.message_handler(commands=['screenshot'])
    def screenshot(message):
        if not is_allowed(bot, message): return
        try:
            filename = system.screenshot()
            with open(filename, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            import os
            os.remove(filename)

        except Exception as e:
            bot.reply_to(message, f"screenshot error: {str(e)}")
    
    @bot.message_handler(commands=['shell'])
def shell(message):
    if not is_allowed(bot, message): return
    try:
        parts = message.text.split(' ', 1)
        if len(parts) < 2:
                bot.reply_to(message, "Usage: /shell <command>\nExample: /shell ls -la")
                return
            bot.reply_to(message, system.shell(parts[1]))
        except Exception as e:
            bot.reply_to(message, f"shell error: {str(e)}")