from pynput import keyboard

def press_callback(key):
    print('{} was pressed'.format(key))

l = keyboard.Listener(on_press=press_callback)
l.start()
l.join()