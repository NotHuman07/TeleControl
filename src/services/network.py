import subprocess
import re
import time
import logging


logging.basicConfig(level=logging.INFO)
known_devices = set()

def get_devices():
    try:
        result = subprocess.run(['arp-scan', '--localnet'], capture_output=True, text=True)
        ips = re.findall(r'(\d+\.\d+\.\d+\.\d+)', result.stdout)
        return set(ips)
    except Exception as e:
        logging.error(f"Error occurred while fetching devices: {e}")
        return set() 

def watch_network(bot, chat_id):
    
    global known_devices
    known_devices = get_devices()
    while True:
        try:
            time.sleep(60)
            current = get_devices()
            new = current - known_devices
            if new:
                for ip in new:
                    bot.send_message(chat_id, f"New device detected: {ip}")
            known_devices = current
        except Exception as e:
            logging.error(f"watch_network error: {e}")
