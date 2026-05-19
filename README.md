# 🦅 TeleControl

Control and monitor your Linux machine remotely through Telegram.
No app needed. No third-party software. Just your bot and your machine.

---

## 🚀 What It Does

| Command | Description |
|---|---|
| /start | Activate the bot |
| /wifi | Scan and show all devices on your network |
| /cpu | Show current processor usage |
| /disk | Show storage information |
| /temp | Show CPU temperature |
| /screenshot | Capture and send your screen |
| /shell <cmd> | Run any terminal command remotely |

Auto-Alert: Bot automatically notifies you when a new device joins your WiFi network.

---

## 🛡️ Security

- Whitelist-only access — unauthorized users are blocked and logged
- Secrets managed via .env — never hardcoded
- Every action logged with timestamp and username
- Runs as a systemd service — auto-restarts on crash

---

## 🏗️ Architecture

src/
├── handlers.py         # Telegram command logic
├── services/
│   ├── system.py       # CPU, disk, temp, screenshot, shell
│   └── network.py      # ARP scanning, auto-alert
└── utils/
└── auth.py         # Whitelist authentication

---

## ⚙️ Setup

1. Clone the repo
```bash
git clone https://github.com/NotHuman07/TeleControl.git
cd TeleControl

2. Install dependencies

pip install -r requirements.txt


3. Create .env file

BOT_TOKEN=your_telegram_bot_token
ADMIN_ID=your_telegram_chat_id
ALLOWED_USERS=your_chat_id


4. Run

python3 main.py


5. Run as a service (auto-restart)

sudo systemctl enable falconbot
sudo systemctl start falconbot


🧪 Run Tests

python3 tests/test_system.py


🛠️ Built With

 • Python 3
 • pyTelegramBotAPI
 • Linux (tested on Linux Mint)
 • systemd
 • arp-scan

📌 Roadmap

 • SQLite audit logging
 • Multi-user support with invite system
 • OS detection for Windows/Mac support
 • Cloud deployment
 • End-to-end encryption

👤 Author

[Muaasid Mahamad] — CSE AI Graduate
Built this to learn Python, Linux, APIs and system architecture from scratch.


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

