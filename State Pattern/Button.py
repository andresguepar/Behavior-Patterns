from OffState import OffState 
class Button:
    def __init__(self):
        self.state = OffState(self)

    def change_state(self, state):
        self.state = state

    def off(self):
        self.state.off()

    def locked(self):
        self.state.locked()

    def ready(self):
        self.state.ready()