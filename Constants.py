from Xlib import XK

UP_KEY = "up"
DOWN_KEY = "down"
LEFT_KEY = "left"
RIGHT_KEY = "right"
 
LEFT_CLICK = "page_up"    # Numpad 9
RIGHT_CLICK = "page_down"   # Numpad 3
 
TOGGLE_KEY = "tab"   # Change this to whatever key you want


KEY_MAP = {
    "up":       XK.XK_Up,
    "down":     XK.XK_Down,
    "left":     XK.XK_Left,
    "right":    XK.XK_Right,
    "page up":  XK.XK_Page_Up,
    "page down":XK.XK_Page_Down,
    "9":        XK.XK_KP_9,
    "3":        XK.XK_KP_3,
    "f8":       XK.XK_F8,
    "escape":   XK.XK_Escape,
}
