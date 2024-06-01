from IClient import IClient

class Gold(IClient):
    def __init__(self, name):
        self.name = name
    
    def accept(self, visitor):
        visitor.visitGold(self)