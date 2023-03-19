from tkinter import *
from tkinter import ttk
import mouse

is_recording = False

def record_actions(actions, action_details, actionsvar, is_recording):
    is_recording = True
    mouse.hook(lambda event: mouse_action(actions, action_details, actionsvar, is_recording, event))

def stop_recording(is_recording):
    is_recording = False
    # mouse.unhook_all()

def mouse_action(actions, action_details, actionsvar, is_recording, event):
    if is_recording == False:
        mouse.unhook_all()
    else:
        if(type(event) == mouse._mouse_event.ButtonEvent):
            print(mouse.get_position())
            print(event)
            print(event.time)
            print(event.button + " | " + event.event_type + " | " + str(event.time))

            actions.append(event.button + " | " + event.event_type + " | " + str(event.time))
            action_details.append({"action": event.button, "time": event.time, "mouse_position": mouse.get_position()})
            actionsvar.set(actions)

root = Tk()
root.title("Macro Maker")

menu_frame = ttk.Frame(root)

actions = []
action_details = []
actionsvar = StringVar(value=actions)

record_button = ttk.Button(menu_frame, text="Record", command=lambda : record_actions(actions, action_details, actionsvar, is_recording))
stop_button = ttk.Button(menu_frame, text="Stop", command=stop_recording(is_recording))

action_list = Listbox(menu_frame, height=10, listvariable=actionsvar)

menu_frame.grid(column=0, row=0)
record_button.grid(column=0, row=0)
stop_button.grid(column=1, row=0)
action_list.grid(column=0, row = 2, columnspan=3)

actions = []
actionsvar.set(actions)

root.mainloop()

