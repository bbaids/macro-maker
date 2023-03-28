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
        self.interrupt = False
        keyboard.add_hotkey('esc', self.set_interrupt)
        print('playing')

        if self.is_recording:
            print("Please stop your recording first")
        else:      
            while self.loop_play:  
                print('looped')
                if self.interrupt:
                    break
                self.execute_actions()
            else: 
                print('non-looped')
                self.execute_actions()

    def execute_actions(self):
        print('Executing')
        print(self.interrupt)
        for action in self.curr_rec.actions:
            if self.interrupt:
                    break
            move_duration = .1  
            time.sleep(action['delay'] - move_duration)
            mouse.move(action['position'][0], action['position'][1], duration=move_duration)
            mouse.click()
            

    def toggle_loop(self):
        self.loop_play = not self.loop_play

    def set_interrupt(self):
        print("Interrupting")
        self.interrupt = True
        keyboard.remove_all_hotkeys()