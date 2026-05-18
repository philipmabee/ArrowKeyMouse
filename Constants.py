from pynput import keyboard
from Xlib import XK
 
UP_KEY = keyboard.Key.up
DOWN_KEY = keyboard.Key.down
LEFT_KEY = keyboard.Key.left
RIGHT_KEY = keyboard.Key.right
 
LEFT_CLICK = keyboard.Key.shift_r
RIGHT_CLICK = keyboard.Key.enter
 
TOGGLE_KEY = keyboard.Key.alt_l  # Change this to whatever key you want

SPEED_UP_KEY = keyboard.Key.page_up
SPEED_DOWN_KEY = keyboard.Key.page_down
MOUSE_SPEED = 18  # Adjust this for faster/slower movement
# Xlib keysyms for suppression (must match the keys above)
SUPPRESSED_KEYSYMS = [
    XK.XK_Up, XK.XK_Down, XK.XK_Left, XK.XK_Right,
    XK.XK_Shift_R, XK.XK_KP_Enter,
    XK.XK_Page_Up, XK.XK_Page_Down
]
