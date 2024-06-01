from IClient import IClient

class Platinum(IClient):
    def __init__(self, name):
        self.name = name
    
    def accept(self, visitor):
        visitor.visitPlatinum(self)