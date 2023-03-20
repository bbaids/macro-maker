import keyboard
import time

run = True
print(run)
def stop():
    nonlocal run
    print(run)
    print('trying to stop')
    run = False
    print(run)

keyboard.on_press_key('esc', lambda event: stop(run))

while run:
    print("running")
    time.sleep(1)

