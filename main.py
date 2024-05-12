import os
import random
import threading
import time
import wave
import pyaudio
from pynput import mouse, keyboard

sounds = []
release_sounds = []
old_key = None
running = True

for filename in os.listdir("sounds"):
    if filename.endswith(".wav"):
        sounds.append(filename)

for filename in os.listdir("release_sounds"):
    if filename.endswith(".wav"):
        release_sounds.append(filename)

lock1 = threading.Lock()
def play_sound():
    if sounds:
        number = random.randint(0, len(sounds) - 1)
        try:
            with lock1:
                wf = wave.open("sounds/" + sounds[number], 'rb')
                p = pyaudio.PyAudio()
                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)
                data = wf.readframes(1024)
                while data:
                    stream.write(data)
                    data = wf.readframes(1024)
                stream.stop_stream()
                stream.close()
                p.terminate()
        except Exception as e:
            print("Error playing sound:", sounds[number])


lock2 = threading.Lock()


def play_release_sound(e):
    if release_sounds:
        number = random.randint(0, len(release_sounds) - 1)
        try:
            with lock2:
                wf = wave.open("release_sounds/" + release_sounds[number], 'rb')
                p = pyaudio.PyAudio()
                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)
                data = wf.readframes(1024)
                while data:
                    stream.write(data)
                    data = wf.readframes(1024)
                stream.stop_stream()
                stream.close()
                p.terminate()
        except Exception as e:
            print("Error playing sound:", release_sounds[number])


def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            sound_thread = threading.Thread(target=play_sound)
            sound_thread.daemon = True
            sound_thread.start()


def on_press(key):

    global old_key, running
    if key in [keyboard.Key.space, keyboard.Key.up] and old_key != key:
        sound_thread = threading.Thread(target=play_sound)
        sound_thread.daemon = True
        sound_thread.start()
    old_key = key

    # Check for Ctrl + Q to stop the main function
    if key == keyboard.KeyCode.from_char('`'):
        running = False


def on_release(key):
    global old_key
    if key in [keyboard.Key.space, keyboard.Key.up]:
        sound_thread = threading.Thread(target=play_release_sound)
        sound_thread.daemon = True
        sound_thread.start()


listener_mouse = mouse.Listener(on_click=on_click)
listener_keyboard = keyboard.Listener(on_press=on_press, on_release=on_release)
listener_mouse.start()
listener_keyboard.start()

while running:
    time.sleep(0.1)


listener_mouse.stop()

