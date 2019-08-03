import numpy as np
import yaml

uint = lambda x: int(x) if x > 0 else 0
check = lambda x: int(x) if x < 1000 else int(1500)

class Environnement():
    def __init__(self):
        self.stock = {}
        self.price = {}
        self.exchange = []
        self.whatThePeopleTake = 10
        self.setup()
        self.turnOver()

    def setup(self):
        with open("config/environnement.yml", 'r') as stream:
            data_loaded = yaml.safe_load(stream)

        self.exchange = data_loaded["Exchange"]
        del data_loaded["Exchange"]
        
        for key in data_loaded.keys():
            self.stock[key] = data_loaded[key]["Amount"]

    def showEnvironnementStock(self):
        print("Stock: {}".format(self.stock))
    
    def showEnvironnementPrice(self):
        print("Price: {}".format(self.price))

    def sellStock(self,product,amount):
        self.stock[product] += amount
        return self.price[product]*amount

    def buyStock(self,product,amount):
        self.stock[product] -= amount
        return self.price[product]*amount

    def turnOver(self):
        for key in self.stock.keys():
            self.stock[key] = uint(self.stock[key] - self.whatThePeopleTake)
            self.price[key] = check(uint(10000/(self.stock[key]+1)))

        for key in self.stock.keys():
            upgrade = 1
            if (self.stock[key] < 1000):
                upgrade = 0
        if (upgrade == 1):
            self.whatThePeopleTake += 10

if __name__ == "__main__":
    a = Environnement()
    a.showEnvironnementPrice()
    a.showEnvironnementStock()