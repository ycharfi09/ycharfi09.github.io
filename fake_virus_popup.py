import tkinter as tk
from tkinter import messagebox
import time
import threading

def show_message():
    # Show a scary popup
    time.sleep(1)
    messagebox.showwarning("Virus Detected", "Warning: A virus has been installed on your system!")
    time.sleep(2)
    messagebox.showinfo("Just Kidding", "Nah... this is just a prank 😄")
    root.quit()

# Setup fake window
root = tk.Tk()
root.title("Virus Installer")
root.geometry("300x150")
root.configure(bg="#300000")
root.resizable(False, False)

label = tk.Label(root, text="Installing virus...", font=("Segoe UI", 14), fg="white", bg="#300000")
label.pack(expand=True)

# Run popup in another thread to avoid freezing the window
threading.Thread(target=show_message).start()

# Start GUI loop
root.mainloop()
