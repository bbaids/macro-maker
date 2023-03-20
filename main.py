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
        if not self.is_empty:
            self.actions = []
            play_button.forget()
        
        self.is_recording = True
        self.is_empty = False
        print("Now Recording")
        mouse.on_click(self.record_click)

    def record_click(self):
        if self.is_recording:
            self.actions.append({
                "action": "left",
                "position": mouse.get_position(),
                "time": time.time()
            })

    def stop_recording(self):
        self.is_recording = False
        mouse.unhook_all()

        #Process the recorded actions
        recording_length = len(self.actions)
        print(recording_length)
        for i in range(0, recording_length):
            if i == recording_length - 2:
                self.actions.pop()
                break
            else:
                print(i)
                self.actions[i]['delay'] = self.actions[i+1]['time'] - self.actions[i]['time']

        play_button.grid(column=3, row=0)

    def play_recording(self):
        if self.is_recording:
            print("Please stop your recording first")
        else:
            print(self.actions)

        for action in self.actions:
            mouse.move(action['position'][0], action['position'][1])
            mouse.click()
            time.sleep(action['delay'])

current_recording = Recording()

root = Tk()
root.title("Macro Maker")

menu_frame = ttk.Frame(root)

record_button = ttk.Button(menu_frame, text="Record", command=current_recording.record)
stop_button = ttk.Button(menu_frame, text="Stop", command=current_recording.stop_recording)
play_button = ttk.Button(menu_frame, text="Play", command=current_recording.play_recording)

menu_frame.grid(column=0, row=0)
record_button.grid(column=0, row=0)
stop_button.grid(column=1, row=0)

root.mainloop()

