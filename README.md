# 🖥️ Keylogger & System Activity Logger (Educational Project)

⚠️ Disclaimer: This project was built strictly for educational and ethical purposes. It must not be used for unauthorized monitoring. The goal is to understand adversarial tactics and defensive strategies.

---
📌 Overview

This project simulates an adversary tool that captures user activity and exfiltrates data via email. It provides hands-on practice in understanding how attackers operate, and how defenders can detect and mitigate such behaviors.

## ⚡ Features

- ⌨️ **Logs keystrokes** (enabled via `ENABLE_KEYLOGGER`).  
- 📸 **Captures screenshots** (enabled via `ENABLE_SCREENSHOTS`).  
- 🖥️ **Collects system info** (OS, version, CPU, IP addresses).  
- 📧 **Sends logs and screenshots via email**.  
- 🌐 **Cross-platform support**: Windows, Linux, macOS.  
- 🗂️ **Maintains a hidden runtime folder** `.runtime` for logs and screenshots.  
- 🧹 **Cleans up** `.runtime` and `__pycache__` on exit.  

---

## 🚀 Example Output


```text
✅ Keylogger enabled
📸 Screenshot saved: .runtime/screenshots/screen_2025-08-24_12-34-56.png
📧 Email sent successfully with screen_2025-08-24_12-34-56.png, keylog.txt, system_info.xlsx
🗑️ Removed folder: .runtime/screenshots
🧹 Cleared file: .runtime/keylog.txt
🧹 Cleared Excel file: .runtime/system_info.xlsx
✅ Cleanup complete: Screenshots, logs, Excel, venv, and __pycache__ cleared.
```

---

## 🗂️ Project Structure

```text
Keylogger/
│
├─ .gitignore
├─ README.md
├─ config.py          # Configurations and helper functions
├─ main.py            # Main executable script
├─ requirements.txt   # Python dependencies
└─ .runtime/          # Hidden folder for runtime data
   ├─ screenshots/
   ├─ keylog.txt
   └─ system_info.xlsx
```
---

## ⚙️ **Setup Instructions**

### 1. Clone the repository
```bash
git clone  https://github.com/barxiii/Keylogger.git
cd Keylogger
```

### 2. Install Python dependencies (Optional)
```bash
pip install -r requirements.txt
```
> ***The code automatically checks and installs the dependencies at each run***
>>***On Kali Linux: the code automatically uses --break-system-packages for pip installs.***

### 3. Configure Email Settings

Before running the keylogger, you need to configure the email settings in `config.py`. This is required so the script can send logs and screenshots automatically.

```python
SENDER_EMAIL = "you@example.com"
SENDER_PASSWORD = "yourpassword"
RECEIVER_EMAIL = "receiver@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
```
🔑 Tip: Enable 2FA in Gmail, then generate an App Password for SMTP.

### 4. Run the script

```sh
python main.py
``` 

## 🔧 Configuration Options

| Setting               | Description                             |
| --------------------- | --------------------------------------- |
| `ENABLE_KEYLOGGER`    | Enable keylogging (True/False)          |
| `ENABLE_SCREENSHOTS`  | Enable screenshots (True/False)         |
| `SCREENSHOT_INTERVAL` | Interval in seconds between screenshots |
| `SENDER_EMAIL`        | Sender email address                    |
| `SENDER_PASSWORD`     | Sender email password                   |
| `RECEIVER_EMAIL`      | Recipient email address                 |

---

## 💻 Dependencies

| Module      | Purpose                                |
| ----------- | -------------------------------------- |
| `pyautogui` | Capturing screenshots                  |
| `pynput`    | Keylogging                             |
| `pandas`    | Storing system info                    |
| `openpyxl`  | Excel file handling                    |
| `pillow`    | Image handling (required by pyautogui) |
| `requests`  | Fetching public IP                     |
| `smtplib`   | Sending email (built-in)               |

---

## 📤 Email Sending Logic

❌ If both keylogger and screenshots disabled → exit immediately

📸 If only screenshots enabled → send email every iteration (screenshots + system info)

⌨️ If only keylogger enabled → send email every 5 iterations (keylogs + system info)

📸 + ⌨️ If both enabled → send email every iteration (screenshots), and on 5th iteration include keylog.txt + system_info.xlsx

---
## 🧩 Safety & Testing

- ✅ Enable keylogging and screenshots only in a **controlled lab environment.**

- ⚠️ Do not run on machines without permission — **this tool is for educational purposes.**

---

## 📌 Notes

- Maintains a hidden *.runtime* folder for all runtime data.

- These versions and above should work:
    ✅ Python version: 3.12.0
    ✅ pyautogui version: 0.9.54
    ✅ pandas version: 2.1.2
    ✅ PIL version: 10.1.0
    ✅ openpyxl version: 3.1.5
    ✅ requests version: 2.32.5

- Automatically cleans up *.runtime* and *__ pycache __* on exit.

- Cross-platform support for **Windows, Linux, and macOS**.

---


## 🚀 Next Steps

Planned improvements to expand the project:

🔒 Add AES encryption to logs before sending

🌐 Forward logs into Microsoft Sentinel / Splunk for SIEM detection practice

🖥️ Validate cross-platform (Windows + Linux) behavior

🧑‍💻 Develop a Red vs Blue Lab Exercise (attacker vs defender simulation)

---
## ⚖️ License

MIT License — Educational Use Only

---

## 💸 Support My Work

If you found this project useful and would like to support future cybersecurity projects:

Bitcoin (BTC): 1F81TdYmwCPoDj9FCua5s5KFEY1HLk5gTY

Ethereum (ETH): 0xf776d4593942c0e198ec34fc3c6ce4dc6c236627

USDT (ERC20/TRC20): 0xf776d4593942c0e198ec34fc3c6ce4dc6c236627

🙏 Every little bit helps me continue building practical projects for the cybersecurity community.

