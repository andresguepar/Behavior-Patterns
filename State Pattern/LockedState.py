from State import State


class LockedState(State):
    def locked(self):
        print("El botón está bloqueado")
    def off(self):
        pass

    def ready(self):
        pass