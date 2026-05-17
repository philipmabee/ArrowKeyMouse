from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()
pressed_keys = set()

UP_KEY = keyboard.Key.up
DOWN_KEY = keyboard.Key.down
LEFT_KEY = keyboard.Key.left
RIGHT_KEY = keyboard.Key.right	

LEFT_CLICK = keyboard.Key.enter
RIGHT_CLICK = keyboard.Key.space
