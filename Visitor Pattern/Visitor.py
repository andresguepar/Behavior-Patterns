from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visitVIP(self, vip):
        pass
    
    @abstractmethod
    def visitGold(self, gold):
        pass
    
    @abstractmethod
    def visitPlatinum(self, platinum):
        pass