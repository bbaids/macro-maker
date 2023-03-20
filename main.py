from tkinter import *
from tkinter import ttk
import macroplayer
import recording

root = Tk()
root.title("Macro Maker")

menu_frame = ttk.Frame(root)
mp = macroplayer.MacroPlayer()

record_button = ttk.Button(menu_frame, text="Record", command=mp.start_recording)
stop_button = ttk.Button(menu_frame, text="Stop", command=mp.stop_recording)
play_button = ttk.Button(menu_frame, text="Play", command=mp.play_recording)
loop_checkbox = ttk.Checkbutton(menu_frame, text="Loop Play", command=mp.toggle_loop, variable=mp.loop_play)

menu_frame.grid(column=0, row=0)
record_button.grid(column=0, row=0)
stop_button.grid(column=1, row=0)
play_button.grid(column=2, row=0)
loop_checkbox.grid(column=2, row=1)

root.mainloop()

