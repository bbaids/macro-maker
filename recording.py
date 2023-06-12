class Recording:
    name = None
    actions = []
    loop_around_delay = 1

    def process_recording(self):
        #Process the recorded actions
        recording_length = len(self.actions)
        self.actions[0]['delay'] = self.loop_around_delay
        for i in range(1, recording_length-1):
            self.actions[i]['delay'] = self.actions[i]['time'] - self.actions[i-1]['time']
        #drop the extra action from clicking the stop button
        self.actions.pop()
        self.is_empty = False