from pynput.mouse import Button, Controller
from Xlib import X, XK
from Xlib.display import Display
from Xlib.ext import record
import asyncio
import threading
import struct
from Constants import UP_KEY, DOWN_KEY, LEFT_KEY, RIGHT_KEY, LEFT_CLICK, RIGHT_CLICK, TOGGLE_KEY
 
mouse = Controller()
pressed_keys = set()
suppressing = False
 
display = Display()
root = display.screen().root
 
KEY_MAP = {
    "up":        XK.XK_Up,
    "down":      XK.XK_Down,
    "left":      XK.XK_Left,
    "right":     XK.XK_Right,
    "page up":   XK.XK_Page_Up,
    "page down": XK.XK_Page_Down,
    "9":         XK.XK_KP_9,
    "3":         XK.XK_KP_3,
    "f8":        XK.XK_F8,
    "tab":       XK.XK_Tab,
    "escape":    XK.XK_Escape,
}
 
def name_to_keysym(name):
    return KEY_MAP.get(name.lower())
 
def keysym_to_name(keysym):
    for name, ks in KEY_MAP.items():
        if ks == keysym:
            return name
    return None
 
SUPPRESSED_KEYS = {UP_KEY, DOWN_KEY, LEFT_KEY, RIGHT_KEY, LEFT_CLICK, RIGHT_CLICK}
 
async def waitToRemoveKeys():
    await asyncio.sleep(0.1)
    pressed_keys.clear()
 
async def async_main():
    task = asyncio.create_task(waitToRemoveKeys())
    while not task.done():
        await asyncio.sleep(0.1)
 
def handle_diagonal():
    if len(pressed_keys) < 2:
        return
    if UP_KEY in pressed_keys and RIGHT_KEY in pressed_keys:
        print("up and right pressed")
        mouse.move(20, -20)
    elif UP_KEY in pressed_keys and LEFT_KEY in pressed_keys:
        print("up and left pressed")
        mouse.move(-20, -20)
    elif DOWN_KEY in pressed_keys and RIGHT_KEY in pressed_keys:
        print("down and right pressed")
        mouse.move(20, 20)
    elif DOWN_KEY in pressed_keys and LEFT_KEY in pressed_keys:
        print("down and left pressed")
        mouse.move(-20, 20)
 
def handle_mouse_keys(key):
    if key == LEFT_KEY:
        mouse.move(-20, 0)
    elif key == RIGHT_KEY:
        mouse.move(20, 0)
    elif key == UP_KEY:
        mouse.move(0, -20)
    elif key == DOWN_KEY:
        mouse.move(0, 20)
    elif key == LEFT_CLICK:
        mouse.click(Button.left, 1)
    elif key == RIGHT_CLICK:
        mouse.click(Button.right, 1)
 
def grab_keys():
    for key_name in SUPPRESSED_KEYS:
        keysym = name_to_keysym(key_name)
        if keysym:
            keycode = display.keysym_to_keycode(keysym)
            if keycode:
                root.grab_key(keycode, X.AnyModifier, True,
                              X.GrabModeAsync, X.GrabModeAsync)
    display.flush()
 
def ungrab_keys():
    for key_name in SUPPRESSED_KEYS:
        keysym = name_to_keysym(key_name)
        if keysym:
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
 
def process_event(key, event_type):
    if event_type == 'down':
        if key == TOGGLE_KEY:
            set_suppression(not suppressing)
            return
        if key == "escape":
            print("Exiting...")
            ungrab_keys()
            import os; os.kill(os.getpid(), 9)
 
        pressed_keys.add(key)
        if len(pressed_keys) > 2:
            asyncio.run(async_main())
        print(f"{key} pressed")
        handle_mouse_keys(key)
        handle_diagonal()
    else:
        pressed_keys.discard(key)
 
def event_loop():
    record_display = Display()
 
    ctx = record_display.record_create_context(
        0,
        [record.AllClients],
        [{
            'core_requests': (0, 0),
            'core_replies': (0, 0),
            'ext_requests': (0, 0, 0, 0),
            'ext_replies': (0, 0, 0, 0),
            'delivered_events': (0, 0),
            'device_events': (X.KeyPress, X.KeyRelease),
            'errors': (0, 0),
            'client_started': False,
            'client_died': False,
        }]
    )
 
    def handler(reply):
        if reply.category != record.FromServer:
            return
        if reply.client_swapped:
            return
 
        data = reply.data
        # Each X11 event is 32 bytes
        while len(data) >= 32:
            event_code = data[0] & 0x7f
            keycode = data[1]
            data = data[32:]
 
            if event_code in (X.KeyPress, X.KeyRelease):
                keysym = record_display.keycode_to_keysym(keycode, 0)
                key = keysym_to_name(keysym)
                if key:
                    event_type = 'down' if event_code == X.KeyPress else 'up'
                    process_event(key, event_type)
 
    record_display.record_enable_context(ctx, handler)
    record_display.record_free_context(ctx)
 
print(f"Keyboard hook active. Press {TOGGLE_KEY.upper()} to toggle suppression. Press ESC to exit.")
t = threading.Thread(target=event_loop, daemon=True)
t.start()
t.join()
 
