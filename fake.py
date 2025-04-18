import tkinter as tk
import time
import threading
import random
import winsound
from tkinter import messagebox

# Fake logs for animation
fake_logs = [
    "[*] Establishing connection...",
    "[*] Scanning target network...",
    "[*] Bypassing firewall...",
    "[*] Cracking password hash...",
    "[*] Deploying payload...",
    "[*] Elevating privileges...",
    "[*] Spoofing MAC address...",
    "[*] Reading encrypted volumes...",
    "[+] Privilege escalation successful.",
]

def insert_line(widget, text, delay=0.01):
    for char in text:
        widget.insert(tk.END, char)
        widget.see(tk.END)
        play_typing_sound()
        time.sleep(delay)
    widget.insert(tk.END, "\n")

def play_typing_sound():
    try:
        winsound.Beep(1000, 30)
    except:
        pass

def show_error_spam():
    def spam():
        for _ in range(25):  # Number of popups
            threading.Thread(target=lambda: messagebox.showerror(
                                 "Critical Error",
                                 "Unknown system failure.\nPlease contact your administrator."),
                             daemon=True).start()
            time.sleep(0.2)
        threading.Thread(target=lambda: messagebox.showerror(
                             "JK! This is not a real virus.",
                             "You can close the terminal window from task manager."),
                         daemon=True).start()
    threading.Thread(target=spam, daemon=True).start()

def run_animation(widget):
    for _ in range(30):
        log = random.choice(fake_logs)
        insert_line(widget, log, delay=0.005)
        time.sleep(0.1)

    insert_line(widget, "\n[!] ERROR: SYSTEM UNSTABLE", delay=0.02)
    insert_line(widget, "[!] CRITICAL FAILURE DETECTED", delay=0.02)
    insert_line(widget, "[!] INITIATING FAILSAFE MODE...\n", delay=0.02)

    time.sleep(1)
    show_error_spam()

def on_close():
    pass  # Disable close

# GUI setup
root = tk.Tk()
root.title("Terminal.exe")
root.geometry("900x550")
root.configure(bg="black")
root.protocol("WM_DELETE_WINDOW", on_close)
root.resizable(False, False)

output = tk.Text(root, bg="black", fg="lime", font=("Consolas", 12), borderwidth=0)
output.pack(fill=tk.BOTH, expand=True)

threading.Thread(target=run_animation, args=(output,), daemon=True).start()

root.mainloop()
