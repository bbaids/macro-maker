import keyboard
import mouse
import time

# run = True
# print(run)
# def stop():
#     nonlocal run
#     print(run)
#     print('trying to stop')
#     run = False
#     print(run)

# keyboard.on_press_key('esc', lambda event: stop(run))

# while run:
#     print("running")
#     time.sleep(1)

clicktime = 0

def mouse_call(event):
    global clicktime
    if type(event) == mouse.ButtonEvent:
        if event.event_type == "down":
            clicktime = event.time
        else:
            print(event.time - clicktime)
        

mouse.hook(mouse_call)

while True:
    pass