# main.py

import threading
from control import run_control_window
from listener import listen_for_wake_word
from commands import handle_command

def start_listener():
    listen_for_wake_word(handle_command)

if __name__ == "__main__":
    listener_thread = threading.Thread(target=start_listener, daemon=True)
    listener_thread.start()

    run_control_window()
