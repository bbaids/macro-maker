import mouse
import keyboard
import time
import recording

class MacroPlayer():
    is_recording = False
    loop_play = False
    curr_rec = recording.Recording()
    interrupt = False

    def start_recording(self):
        if not self.curr_rec.is_empty:
            self.curr_rec.actions = []
        
        self.is_recording = True
        print("Now Recording")
        mouse.on_click(self.record_click)

    def record_click(self):
        if self.is_recording:
            self.curr_rec.actions.append({
                "action": "left",
                "position": mouse.get_position(),
                "time": time.time()
            })

    def stop_recording(self):
        self.is_recording = False
        mouse.unhook_all()
        self.curr_rec.process_recording()

    def play_recording(self):
        # keyboard.hook_key('esc', lambda event : self.interrupt)

        if self.is_recording:
            print("Please stop your recording first")
        else:      
            while self.loop_play:  
                self.execute_actions()
            else: 
                self.execute_actions()

    def execute_actions(self):
        for action in self.curr_rec.actions:
            if self.interrupt:
                    break
            mouse.move(action['position'][0], action['position'][1], duration=.25)
            mouse.click()
            time.sleep(action['delay'])

    def toggle_loop(self):
        self.loop_play = not self.loop_play

    # def interrupt(self):
    #     self.interrupt = True
    #     keyboard.unhook_all()