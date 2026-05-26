# control.py

import tkinter as tk
import config

def start_nova():
    config.ASSISTANT_ON = True
    status_label.config(text="Status: ON", fg="green")

def stop_nova():
    config.ASSISTANT_ON = False
    status_label.config(text="Status: OFF", fg="red")

def run_control_window():
    global status_label

    root = tk.Tk()
    root.title("Nova Assistant")
    root.geometry("220x150")
    root.resizable(False, False)

    status_label = tk.Label(root, text="Status: OFF", fg="red", font=("Arial", 12))
    status_label.pack(pady=10)

    tk.Button(root, text="Start Nova", width=15, command=start_nova).pack(pady=5)
    tk.Button(root, text="Stop Nova", width=15, command=stop_nova).pack(pady=5)
    tk.Button(root, text="Exit", width=15, command=root.destroy).pack(pady=5)

    root.mainloop()
