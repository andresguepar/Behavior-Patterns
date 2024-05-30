class Employee:
    def __init__(self,name,positions):
        self.name = name
        self.positions = positions
        self.subordinates = []

    def add_subordinates(self,subordinate):
        self.subordinates.append(subordinate)

    def __str__(self):
        return f'{self.name}({self.positions})'