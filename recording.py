class Recording:
    is_empty = True
    actions = []
    name = None

    def process_recording(self):
        if self.is_empty:
            #Process the recorded actions
            recording_length = len(self.actions)
            for i in range(0, recording_length):
                if i == recording_length - 1:
                    self.actions.pop()
                    break
                else:
                    self.actions[i]['delay'] = self.actions[i+1]['time'] - self.actions[i]['time']

            self.is_empty = False


