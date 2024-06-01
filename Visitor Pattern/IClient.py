from abc import ABC, abstractmethod


class IClient(ABC):
    
    @abstractmethod
    def accept(self, visitor):
        pass
