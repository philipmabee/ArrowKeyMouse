#!/usr/bin/env python3

import platform
from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep
from Constants import UP_KEY, DOWN_KEY, LEFT_KEY, RIGHT_KEY, LEFT_CLICK, RIGHT_CLICK, TOGGLE_KEY, MOUSE_SPEED, SPEED_UP_KEY, SPEED_DOWN_KEY, KB_TO_PYNPUT

OS = platform.system()
mouse = Controller()
mouse_dir = [0, 0]  # x, y
suppressing = False

# ====================== Platform-specific suppression ======================

if OS == "Linux":
		from Xlib import X
		from Xlib.display import Display
		from Constants import SUPPRESSED_KEYSYMS

		display = Display()
		root = display.screen().root

		def grab_keys():
				for keysym in SUPPRESSED_KEYSYMS:
						keycode = display.keysym_to_keycode(keysym)
						if keycode:
								root.grab_key(keycode, X.AnyModifier, True,
															X.GrabModeAsync, X.GrabModeAsync)
				display.flush()

		def ungrab_keys():
				for keysym in SUPPRESSED_KEYSYMS:
						keycode = display.keysym_to_keycode(keysym)
						if keycode:
								root.ungrab_key(keycode, X.AnyModifier)
				display.flush()

		def set_suppression(state):
				global suppressing
				suppressing = state
				if suppressing:
						grab_keys()
						print("Suppression ON")
				else:
						ungrab_keys()
						print("Suppression OFF")

elif OS == "Windows":
		import keyboard as kb
		from Constants import SUPPRESSED_KEY_NAMES

		win_hook = None

		def win_handler(event):
				if event.event_type != "down":
						return
				pynput_key = KB_TO_PYNPUT.get(event.name)
				if pynput_key:
						on_press(pynput_key)

		def set_suppression(state):
				global suppressing, win_hook
				suppressing = state
				if suppressing:
						if win_hook:
								kb.unhook(win_hook)
						win_hook = kb.hook(win_handler, suppress=True)
						print("Suppression ON")
				else:
						if win_hook:
								kb.unhook(win_hook)
								win_hook = None
						print("Suppression OFF")

else:
		def set_suppression(state):
				global suppressing
				suppressing = state
				print(f"Suppression {'ON' if state else 'OFF'} (unsupported on {OS})")

# ====================== Input handling ======================

def on_press(key):
		global MOUSE_SPEED
		if key == SPEED_UP_KEY:
				MOUSE_SPEED += 2
				print(f"Mouse speed increased to {MOUSE_SPEED}")
				return
		if key == SPEED_DOWN_KEY:
				MOUSE_SPEED -= 2
				print(f"Mouse speed decreased to {MOUSE_SPEED}")
				return
		if key == TOGGLE_KEY:
				set_suppression(not suppressing)
				return

		if key == LEFT_KEY:
				mouse_dir[0] = -MOUSE_SPEED
		elif key == RIGHT_KEY:
				mouse_dir[0] = MOUSE_SPEED
		elif key == UP_KEY:
				mouse_dir[1] = -MOUSE_SPEED
		elif key == DOWN_KEY:
				mouse_dir[1] = MOUSE_SPEED
		elif key == LEFT_CLICK:
				mouse.click(Button.left)
		elif key == RIGHT_CLICK:
				mouse.click(Button.right)

def on_release(key):
		if key == LEFT_KEY:
				mouse_dir[0] = 0
		elif key == RIGHT_KEY:
				mouse_dir[0] = 0
		elif key == UP_KEY:
				mouse_dir[1] = 0
		elif key == DOWN_KEY:
				mouse_dir[1] = 0

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

print(f"Running on {OS}. Press {TOGGLE_KEY} to toggle suppression.")

while True:
		mouse.move(mouse_dir[0], mouse_dir[1])
		sleep(0.02)
