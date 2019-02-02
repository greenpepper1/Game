from stock import stock
from envirnement import Environment

environment = Environment()

class Building():
    def showStock(self):
        print("Building stock")
        print(self.stock)
        print("")

    def baseRunningCosts(self):
        self.stock["water"] -= 5
        self.stock["electric"] -= 5

    def setStock(self,stock):
        self.stock = stock

    def getStock(self):
        return self.stock

    def sellProduce(self):
        if(self.stock[self.product] > 0):
            self.stock["cash"] += self.environment.sellStock(self.product,self.stock[self.product])
            self.stock[self.product] = 0

    def buyProduce(self,product):
        self.stock["cash"] -= self.environment.buyStock(product,55) ## Need to adjust the cash not set it!
        self.stock[product] += 55

    def checkIfZero(self):
        if(not(all(value > -1 for value in self.stock.values()))):
            # print(self.stock)
            for product in self.stock.keys():
                if self.stock[product] < 0 and not(product=="cash"):
                    self.buyProduce(product)

    def turnOver(self):
        self.stock["cash"] -= 10

        self.checkIfZero()
        self.baseRunningCosts()
        self.specialRunningCosts()
        self.manufacture()
        self.sellProduce()
        self.environment.showEnvironmentStock()
        self.environment.turnOver()

class Mine(Building):
    def __init__(self):
        self.product = "minerals"
        self.stock = stock
        self.environment = environment

    def specialRunningCosts(self):
        self.stock["water"] -= 5
        self.stock["electric"] -= 20

    def manufacture(self):
        self.stock[self.product] += 50

class Farm(Building):
    def __init__(self):
        self.product = "food"
        self.stock = stock
        self.environment = environment

    def specialRunningCosts(self):
        self.stock["water"] -= 35
        self.stock["electric"] -= 20

    def manufacture(self):
        self.stock[self.product] += 50

class PowerPlant(Building):
    def __init__(self):
        self.product = "electric"
        self.stock = stock
        self.environment = environment

    def specialRunningCosts(self):
        self.stock["minerals"] -= 50

    def manufacture(self):
        self.stock[self.product] += 25

class Factory(Building):
    def __init__(self):
        self.product = "alloys"
        self.stock = stock
        self.environment = environment

    def specialRunningCosts(self):
        self.stock["minerals"] -= 50
        self.stock["electric"] -= 50

    def manufacture(self):
        self.stock[self.product] += 25

Buildings = [Mine(), Farm(), PowerPlant(), Factory()]
