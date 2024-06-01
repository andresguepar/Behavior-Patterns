from IClient import IClient

class Vip(IClient):
    
    def __init__(self, name):
        self.name = name
    
    def accept(self, visitor):
        visitor.visitVIP(self)