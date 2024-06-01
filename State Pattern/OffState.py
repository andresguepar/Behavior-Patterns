
from State import State


class OffState(State):
    def off(self):
        print("El botón está apagado")
    def locked(self):
        pass

    def ready(self):
        pass
    