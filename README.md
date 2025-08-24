# 🔑 Keylogger Project


A **cross-platform Python keylogger and system monitoring tool** that collects system information, captures screenshots, logs keystrokes, and can send data via email. Designed for **educational and ethical lab testing purposes only**.

---

## ⚠️ **Important Notice**

This project is for **educational use in controlled environments only**.  
Do **not** deploy on systems without permission. Unauthorized use may violate laws.

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
git clone  https://github.com/Barryanem/Keylogger.git
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

#### ⚙️ Notes on SMTP & Gmail

SMTP Server: smtp.gmail.com      .............................       (*Any smtp server can be used*)

Port: 465 (SSL)

#### 🔑 Using Gmail Securely

Gmail blocks direct password login for third-party apps for security. To allow sending emails via Python:

- Log in to your Gmail account.

- Go to Manage your Google Account → Security → 2-Step Verification → App passwords.

- Generate a new app password specifically for this script.

- Use this app password as the **SENDER_PASSWORD** instead of your regular Gmail password.

- This ensures the script can send emails securely without compromising your main account password.

⚠️ Do not share your app password. Use this only in a secure, controlled testing environment.

### 4. Run the project

```sh
python main.py
``` 

### 5. Logs & screenshots will be stored in the hidden .runtime folder and automatically emailed based on the configured intervals.
---

## ⚡ Features

- ⌨️ **Logs keystrokes** (enabled via `ENABLE_KEYLOGGER`).  
- 📸 **Captures screenshots** (enabled via `ENABLE_SCREENSHOTS`).  
- 🖥️ **Collects system info** (OS, version, CPU, IP addresses).  
- 📧 **Sends logs and screenshots via email**.  
- 🌐 **Cross-platform support**: Windows, Linux, macOS.  
- 🗂️ **Maintains a hidden runtime folder** `.runtime` for logs and screenshots.  
- 🧹 **Cleans up** `.runtime` and `__pycache__` on exit.  

---


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

## ⚖️ License

MIT License — Educational Use Only


---

## 🚀 Example Output


```text
📸 Screenshot saved: .runtime/screenshots/screen_2025-08-24_12-34-56.png
📧 Email sent successfully with screen_2025-08-24_12-34-56.png, keylog.txt, system_info.xlsx
🗑️ Removed folder: .runtime/screenshots
🧹 Cleared file: .runtime/keylog.txt
🧹 Cleared Excel file: .runtime/system_info.xlsx
✅ Cleanup complete: Screenshots, logs, Excel, venv, and __pycache__ cleared.
```