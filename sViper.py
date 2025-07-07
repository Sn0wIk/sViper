from pynput import mouse
import os
import time
import logging # мне похуй на твои пепы хуепы 
SWIPE_THRESHOLD = 100
swipe_started = False
start_x = 0

def switch_space(direction): # тут я прервался на дрочку
    if direction == "left":
        os.system('osascript -e \'tell application "System Events" to key code 123 using control down\'')  # ←
    else:
        os.system('osascript -e \'tell application "System Events" to key code 124 using control down\'')  # →

def on_click(x, y, button, pressed):
    global swipe_started, start_x
    if button == mouse.Button.middle:
        if pressed:
            swipe_started = True
            start_x = x
        else:
            swipe_started = False

def on_move(x, y):
    global swipe_started, start_x
    if swipe_started:
        dx = x - start_x
        if dx > SWIPE_THRESHOLD:
            logging.info("лево руля")
            switch_space("left")
            swipe_started = False
        elif dx < -SWIPE_THRESHOLD:
            logging.info("право руля")
            switch_space("right")
            swipe_started = False

def main():
    logging.debug("ебашь родной")
    with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
        listener.join()

if __name__ == "__main__":
    main()
