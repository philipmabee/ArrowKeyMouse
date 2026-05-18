from pynput import keyboard
from Xlib import XK
 
UP_KEY = keyboard.Key.up
DOWN_KEY = keyboard.Key.down
LEFT_KEY = keyboard.Key.left
RIGHT_KEY = keyboard.Key.right
 
LEFT_CLICK = keyboard.Key.page_up
RIGHT_CLICK = keyboard.Key.page_down
 
TOGGLE_KEY = keyboard.Key.alt_l  # Change this to whatever key you want
 
# Xlib keysyms for suppression (must match the keys above)
SUPPRESSED_KEYSYMS = [
    XK.XK_Up, XK.XK_Down, XK.XK_Left, XK.XK_Right,
    XK.XK_Page_Up, XK.XK_Page_Down,
]
