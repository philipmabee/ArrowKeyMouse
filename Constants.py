from pynput import keyboard
from Xlib import XK
 
UP_KEY = keyboard.Key.up
DOWN_KEY = keyboard.Key.down
LEFT_KEY = keyboard.Key.left
RIGHT_KEY = keyboard.Key.right
 
LEFT_CLICK = keyboard.Key.shift_r
RIGHT_CLICK = keyboard.Key.enter
 
TOGGLE_KEY = keyboard.Key.alt_l
 
SPEED_UP_KEY = keyboard.Key.tab
SPEED_DOWN_KEY = keyboard.Key.caps_lock
 
MOUSE_SPEED = 18  # Adjust this for faster/slower movement
 
# Xlib keysyms for suppression (must match the keys above)
SUPPRESSED_KEYSYMS = [
    XK.XK_Up, XK.XK_Down, XK.XK_Left, XK.XK_Right,
    XK.XK_Shift_R, XK.XK_Return,   # shift_r and enter
    XK.XK_Tab, XK.XK_Caps_Lock,    # speed up/down
]
KB_TO_PYNPUT = {
		"up": UP_KEY, "down": DOWN_KEY,
		"left": LEFT_KEY, "right": RIGHT_KEY,
		"shift_r": LEFT_CLICK, "enter": RIGHT_CLICK,
		"tab": SPEED_UP_KEY, "caps lock": SPEED_DOWN_KEY,
}
