from State import State


class ReadyState(State):
    def ready(self):
        print("El botón está listo")
        
    def off(self):
        pass

    def locked(self):
        pass
    