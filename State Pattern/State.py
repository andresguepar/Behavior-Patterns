from abc import ABC,abstractmethod

class State(ABC):
    def __init__(self, button):
        self.button = button

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def locked(self):
        pass

    @abstractmethod
    def ready(self):
        pass