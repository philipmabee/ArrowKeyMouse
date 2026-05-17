from pynput.mouse import Button, Controller
from pynput import keyboard
import asyncio
from Constants import UP_KEY, DOWN_KEY, LEFT_KEY, RIGHT_KEY, LEFT_CLICK, RIGHT_CLICK

mouse = Controller()
pressed_keys = set()
async def waitToRemoveKeys():
		await asyncio.sleep(0.1)
		pressed_keys.clear()

async def main():
    # Schedule the job to run concurrently
    task = asyncio.create_task(waitToRemoveKeys())
    
    # Keep doing other things while the job runs
    while not task.done():
        print("Main loop is fully responsive...")
        await asyncio.sleep(0.1)  # Yields control back to the event loop
def on_release(key):
    try:
        pressed_keys.remove(key)
    except KeyError:
        pass
def print_keys_pressed():
	if doublepressed():
		if keyboard.Key.up in pressed_keys and RIGHT_KEY in pressed_keys:
			print("up and right pressed")
			mouse.move(20, -20)

		elif keyboard.Key.up in pressed_keys and LEFT_KEY in pressed_keys:
			print("up and left pressed")
			mouse.move(-20, -20)

		elif keyboard.Key.down in pressed_keys and RIGHT_KEY in pressed_keys:
			print("down and right pressed")
			mouse.move(20, 20)


		elif keyboard.Key.down in pressed_keys and LEFT_KEY in pressed_keys:
			print("down and left pressed")
			mouse.move(-20, 20)

def doublepressed():
	if len(pressed_keys) > 1:
		return True
	else:
		return False

def on_press(key):
		pressed_keys.add(key)
		if len(pressed_keys) > 2:
			asyncio.run(main())
		if hasattr(key, "left"):
			print_keys_pressed()
			# if not doublepressed():
			if key == LEFT_KEY:
					mouse.move(-20, 0) 
			if key == RIGHT_KEY:
					mouse.move(20, 0)
			if key == UP_KEY:
					mouse.move(0, -20)
			if key == DOWN_KEY:
					mouse.move(0, 20)

			if key == LEFT_CLICK:
					mouse.click(Button.left, 1)
			if key == RIGHT_CLICK:
					mouse.click(Button.right, 1)
		print(f"{key} pressed")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


# asyncio.run(main())
