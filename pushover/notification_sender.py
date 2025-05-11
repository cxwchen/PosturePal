import requests
import os
from dotenv import load_dotenv

load_dotenv()

PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")
PUSHOVER_API_TOKEN = os.getenv("PUSHOVER_API_TOKEN")

def send_posture_alert(message="Fix your posture!"):
    url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": PUSHOVER_API_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "message": message
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Notification sent successfully.")
    else:
        print(f"Failed to send notification: {response.text}")
