from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep

mouse = Controller()
mouse_dir = [0, 0] # x, y

def on_press(key):
    if hasattr(key, "left"):
        match key:
            case key.left:
                mouse_dir[0] = -10
            case key.right:
                mouse_dir[0] = 10
            case key.up:
                mouse_dir[1] = -10
            case key.down:
                mouse_dir[1] = 10

            case key.page_up:
                mouse.press(Button.left)
            case key.page_down:
                mouse.press(Button.right)

def on_release(key):
    if hasattr(key, "left"):

        match key:
            case key.left:
                mouse_dir[0] = 0
            case key.right:
                mouse_dir[0] = 0
            case key.up:
                mouse_dir[1] = 0
            case key.down:
                mouse_dir[1] = 0

            case key.page_up:
                mouse.release(Button.left)
            case key.page_down:
                mouse.release(Button.right)

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    mouse.move(mouse_dir[0], mouse_dir[1])
    sleep(0.02)
