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


