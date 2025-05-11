import tkinter as tk
import threading 
import time
from plyer import notification

REMINDER_INTERVAL = 300

def show_overlay_message():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    # root.geometry("400x100+800+500")
    root.configure(bg='red')

    swidth = root.winfo_screenwidth()
    sheight = root.winfo_screenheight()

    windowWidth = 600
    windowHeight = 200

    xpos = (swidth // 2) - (windowWidth // 2)
    ypos = (sheight // 2) - (windowHeight // 2)

    root.geometry(f"{windowWidth}x{windowHeight}+{xpos}+{ypos}")

    label = tk.Label(root, text="Fix your posture!", font=("Helvetica", 24), bg='red')
    label.pack(expand=True)

    root.after(5000, root.destroy)
    root.mainloop()

def periodic_reminder():
    while True:
        threading.Thread(target=show_overlay_message).start()
        notification.notify(
            title='PostureReminder',
            message='Time to fix your posture!',
            timeout=5
        )
        time.sleep(REMINDER_INTERVAL)

if __name__== "__main__":
    print("Posture reminder started... Press Ctrl+C to stop.")
    periodic_reminder()