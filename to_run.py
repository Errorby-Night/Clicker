import keyboard
import subprocess
import os

def start_main():
    print("Running File")
    subprocess.Popen(["python", "main.py"])


def to_exit():
    print("Exiting")
    os._exit(0)


keyboard.add_hotkey('ctrl+shift+y', start_main)
keyboard.add_hotkey('`', to_exit)
keyboard.wait()