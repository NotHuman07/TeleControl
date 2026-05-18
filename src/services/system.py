import subprocess
import os
import time
from src.config import NETSPY_PATH, SCREENSHOT_DIR

def who_is_on_wifi():

    result = subprocess.run(['bash', NETSPY_PATH], capture_output=True, text=True)
    
    import re
    clean = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)
    return clean[:4000] or "No output"

def cpu_usage():

    result = subprocess.run(['top', '-bn1'], capture_output=True, text=True)
    lines = result.stdout.splitlines()[:5]
    return '\n'.join(lines)


def disk_usage():

    result = subprocess.run(['df', '-h'], capture_output=True, text=True)
    return result.stdout[:4000]



def temp():

    result = subprocess.run(['sensors'], capture_output=True, text=True)
    return result.stdout[:4000] or "sensor not installed"

def screenshot():

    filename = f'{SCREENSHOT_DIR}/screen_{int(time.time())}.png'
    os.system(f'scrot {filename}')
    return filename


def shell(cmd):

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = result.stdout or result.stderr
    return output[:4000] or "No Output"
