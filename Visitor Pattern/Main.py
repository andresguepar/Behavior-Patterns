from Vip import Vip
from Gold import Gold
from Platinum import Platinum
from MessageVisitor import MessageVisitor

def main():

    vip_client = Vip("Dolores")
    gold_client = Gold("Marcos")
    platinum_client = Platinum("Polo")

    visitor = MessageVisitor()
    visitor.sendMessage(vip_client) 
    visitor.sendMessage(gold_client)  
    visitor.sendMessage(platinum_client) 

if __name__ == "__main__":
    main()