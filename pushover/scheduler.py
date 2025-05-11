import schedule
import time
from notification_sender import send_posture_alert

# schedule.every(5).minutes.do(send_posture_alert, message="Check your posture!")

print("Starting posture reminder... Press Ctrl+C to stop.")

while True: 
    # schedule.run_pending()
    send_posture_alert()
    time.sleep(300)
