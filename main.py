from pynput import keyboard
import threading
import time

spam_running = False
my_keyboard = keyboard.Controller()
spam_string = "qefzxc"


def on_press(key):
    global spam_running
    if key == keyboard.Key.f6:
        spam_running = not spam_running
        print("ON" if spam_running else "OFF")

def spam():
    time.sleep(3)
    global spam_running
    while True:
        if spam_running == True:
            my_keyboard.type(spam_string)
            time.sleep(0.1)
        else:
            time.sleep(0.1)

spam_thread = threading.Thread(target=spam, daemon=True)
spam_thread.start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

