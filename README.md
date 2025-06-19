Python Keylogger Project (Educational/Research Purposes Only)
This project implements a basic keylogger in Python. It captures keystrokes and periodically sends them to a specified email address. This tool is developed purely for educational purposes to understand how keyboard event handling and email automation work in Python.

Features
Keystroke Capture: Logs alphanumeric keys, spaces, newlines, and provides descriptive tags for special keys (e.g., <BACKSPACE>, <CTRL_L>).

Email Transmission: Sends captured keystrokes via SMTP (e.g., Gmail) to a configurable recipient.

Buffered Sending: Accumulates keystrokes and sends them in batches (every 100 characters) to optimize email frequency.

Configurable Credentials: Email sender/recipient and password are loaded from a config.ini file, ensuring sensitive data is not hardcoded or committed to version control.

Ethical Considerations and Disclaimer
CRITICAL WARNING: Keyloggers are powerful tools that can be used for malicious purposes, such as unauthorized surveillance.

THIS PROJECT IS FOR EDUCATIONAL AND ETHICAL RESEARCH PURPOSES ONLY.

Unauthorized use of this software is illegal and unethical.

ALWAYS obtain explicit, written consent from individuals and the owner of the computer system before deploying or testing this code.

This project demonstrates a technical capability. I strongly condemn and advise against its use for any illegal, unethical, or harmful activities.

By using this code, you assume full responsibility for its use and any consequences that may arise.

Prerequisites
Python 3.x installed.

pynput library.

An email account (e.g., Gmail) configured to allow "App passwords" for programmatic access. If using Gmail, "Less secure app access" is deprecated; you must use an App password.

Installation
Clone the repository:

git clone https://github.com/jagadaprarthana/python-keylogger.git
cd python-keylogger

Install dependencies:

pip install -r requirements.txt

Create config.ini:
IMPORTANT: This file contains sensitive credentials and SHOULD NOT BE UPLOADED TO GITHUB. Create a file named config.ini in the root of your project directory with the following content:

[EMAIL]
from_email = your_sending_email@gmail.com
to_email = your_receiving_email@example.com
password = your_generated_app_password

Replace placeholders with your actual email credentials. For Gmail, password must be an App password.

Usage
Ensure you have created and configured config.ini as described above.

Run the script from your terminal:

python keylogger.py

The keylogger will start running in the background. Keystrokes will be collected and sent via email when the buffer reaches 100 characters.

To stop the keylogger, press Ctrl+C in the terminal where it's running.

How It Works
The script uses the pynput library to create a keyboard listener (pynput.keyboard.Listener). The log_happykey function is called every time a key is pressed. This function appends the key to a global keystrokes buffer. When the buffer reaches a certain length (100 characters), the send_email_with_content function is invoked. This function uses Python's built-in smtplib and email.mime modules to construct and send an email containing the collected keystrokes to the configured recipient. Email credentials are securely loaded from config.ini at runtime.

Contributing
Feel free to open issues or submit pull requests for any improvements or bug fixes. Please adhere to strict ethical guidelines for any contributions.

License
This project is licensed under the MIT License.