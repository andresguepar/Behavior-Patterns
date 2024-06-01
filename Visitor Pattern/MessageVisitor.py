from Visitor import Visitor

class MessageVisitor(Visitor):

    def sendMessage(self, client):
        client.accept(self)
    
    def visitVIP(self, vip):
        print("Sending VIP message to", vip.name)
    
    def visitGold(self, gold):
        print("Sending Gold message to", gold.name)
    
    def visitPlatinum(self, platinum):
        print("Sending Platinum message to", platinum.name)