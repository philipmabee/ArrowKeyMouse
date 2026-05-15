
import time

from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()
pressed_keys = set()
# keys = set()
def on_release(key):
    try:
        pressed_keys.remove(key)
    except KeyError:
        pass
def print_keys_pressed():
	if doublepressed():
		if keyboard.Key.up in pressed_keys and keyboard.Key.right in pressed_keys:
			pressed_keys.add(keyboard.Key.up)
			pressed_keys.add(keyboard.Key.right)
			print("up and right pressed")

		elif keyboard.Key.up in pressed_keys and keyboard.Key.left in pressed_keys:
			pressed_keys.add(keyboard.Key.up)
			pressed_keys.add(keyboard.Key.left)
			print("up and left pressed")

		elif keyboard.Key.down in pressed_keys and keyboard.Key.right in pressed_keys:
			pressed_keys.add(keyboard.Key.down)
			pressed_keys.add(keyboard.Key.right)
			print("down and right pressed")

		elif keyboard.Key.down in pressed_keys and keyboard.Key.left in pressed_keys:
			pressed_keys.add(keyboard.Key.down)
			pressed_keys.add(keyboard.Key.left)
			print("down and left pressed")

def doublepressed():
	if len(pressed_keys) > 1:
		return True
	else:
		return False

# 		return True
# 	else:
# 		return False

def on_press(key):
		pressed_keys.add(key)
		if hasattr(key, "left"):
			print_keys_pressed()
			# if not doublepressed():
			if key == key.left:
					mouse.move(-20, 0) 
			if key == key.right:
					mouse.move(20, 0)
			if key == key.up:
					mouse.move(0, -20)
			if key == key.down:
					mouse.move(0, 20)

			# if doublepressed():
			if pressed_keys == {keyboard.Key.up, keyboard.Key.right}:
				mouse.move(20, -20)
				pressed_keys.remove(keyboard.Key.up)
				pressed_keys.remove(keyboard.Key.right)

			elif pressed_keys == {keyboard.Key.up, keyboard.Key.left}:
				mouse.move(-20, -20)
				pressed_keys.remove(keyboard.Key.up)
				pressed_keys.remove(keyboard.Key.left)

			elif pressed_keys == {keyboard.Key.down, keyboard.Key.right}:
				mouse.move(20, 20)
				pressed_keys.remove(keyboard.Key.down)
				pressed_keys.remove(keyboard.Key.right)

			elif pressed_keys == {keyboard.Key.down, keyboard.Key.left}:
				mouse.move(-20, 20)
				pressed_keys.remove(keyboard.Key.down)
				pressed_keys.remove(keyboard.Key.left)

			if key == key.page_up:
					mouse.click(Button.left, 1)
			if key == key.page_down:
					mouse.click(Button.right, 1)
		print(f"{key} pressed")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


# yooooooooo
