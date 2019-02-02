from buildings import Buildings
from stock import stock
from random import randint, choice
from copy import deepcopy

# print(randint(0, 9))
# random.choice(d.keys())

class Business():
    def __init__(self):
        self.holdings = [choice(Buildings)]
        self.stock = deepcopy(stock)

    def showHoldings(self):
        for hold in self.holdings:
            print(hold.product)

    def turnOver(self):
        for hold in self.holdings:
            hold.setStock(self.stock)
            hold.turnOver()
            hold.getStock()

    def showStock(self):
        print("Business stock")
        print(self.stock)
        print("")
