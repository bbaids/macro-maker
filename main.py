from tkinter import *
from tkinter import ttk
import mouse
import time

class Recording:
    is_empty = True
    is_recording = False
    actions = []
    name = None

    def record(self):
        self.is_recording = True
        self.is_empty = False
        print("Now Recording")
        mouse.on_click(self.record_click)

    def play(self):
        print(self.actions)

    def record_click(self):
        if self.is_recording:
            self.actions.append({
                "action": "left",
                "position": mouse.get_position(),
                "time": time.time(),
                "delay": lambda : 0 if len(self.actions) == 0 else 
            })

        print(len(self.actions))

    def stop_recording(self):
        if self.is_recording:
            self.actions.pop()
        self.is_recording = False
        mouse.unhook_all()
        

    def read_recording(self):
        if self.is_recording:
            print("Please stop your recording first")
        else:
            print(self.actions)

current_recording = Recording()

root = Tk()
root.title("Macro Maker")

menu_frame = ttk.Frame(root)

record_button = ttk.Button(menu_frame, text="Record", command=current_recording.record)
stop_button = ttk.Button(menu_frame, text="Stop", command=current_recording.stop_recording)
read_button = ttk.Button(menu_frame, text="Read", command=current_recording.read_recording)

menu_frame.grid(column=0, row=0)
record_button.grid(column=0, row=0)
stop_button.grid(column=1, row=0)
read_button.grid(column=2, row=0)

root.mainloop()

