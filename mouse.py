from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep

mouse = Controller()
mouse_dir = [0, 0] # x, y

def on_press(key):
    if hasattr(key, "left"):
        if key == key.left:
            mouse_dir[0] = -10
        if key == key.right:
            mouse_dir[0] = 10
        if key == key.up:
            mouse_dir[1] = -10
        if key == key.down:
            mouse_dir[1] = 10

        if key == key.page_up:
            mouse.click(Button.left)
        if key == key.page_down:
            mouse.click(Button.right)

def on_release(key):
    if hasattr(key, "left"):
        if key == key.left:
            mouse_dir[0] = 0
        if key == key.right:
            mouse_dir[0] = 0
        if key == key.up:
            mouse_dir[1] = 0
        if key == key.down:
            mouse_dir[1] = 0

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    mouse.move(mouse_dir[0], mouse_dir[1])
    sleep(0.02)
