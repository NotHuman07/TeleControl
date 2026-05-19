# 🛠️ TeleMonitor

A lightweight **remote monitoring and management** tool for Linux machines using Telegram Bot.  

No heavy apps, no third-party services — just a simple bot that helps you monitor and manage your personal Linux machine remotely.

---

## ✨ Features

- Real-time system monitoring (CPU, Disk, Temperature)
- Network device discovery (WiFi/ARP scan)
- Screenshot capture
- Remote shell execution (for authorized users only)
- Automatic alerts when new devices join your network
- Runs reliably as a systemd service

---

## 🛡️ Security & Responsible Use

- **Whitelist-only access** — Only pre-approved Telegram users can interact
- All actions are logged with timestamps
- Credentials managed securely via `.env`
- Built strictly for **personal and educational use** on your own machines
- Requires explicit consent for any deployment

> **Important**: This tool is intended for monitoring **your own devices** only. Always respect privacy and applicable laws.

---

## 📂 Project Structure

```bash
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── handlers.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── network.py
│   │   └── system.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── auth.py
│       └── logger.py
│
└── tests/
    ├── __init__.py
    └── test_system.py


⚙️ Setup

Clone the repository:Bashgit clone https://github.com/NotHuman07/TeleMonitor.git
cd TeleMonitor
Install dependencies:Bashpip install -r requirements.txt
Create a .env file:envBOT_TOKEN=your_telegram_bot_token_here
ALLOWED_USERS=your_telegram_user_id
Run the bot:Bashpython3 main.py
(Recommended) Run as systemd service for persistence:Bashsudo cp falconbot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now falconbot


🧪 Testing
Bashpython3 -m pytest tests/    # or run individual test files

🛠️ Tech Stack

Python 3.8+
pyTelegramBotAPI
systemd (for service)
arp-scan (network discovery)
psutil, Pillow, etc.


📌 Future Improvements

SQLite-based audit logging
Web dashboard (FastAPI + React)
Basic cross-platform support (Windows)
Docker support
Improved encryption for sensitive commands


👤 About Me
[Muaasid Mahamad]
Built this project to strengthen my skills in Python, Linux system programming, API integration, and background services.

Disclaimer: This project is for learning and personal use. Please use responsibly and ethically.

