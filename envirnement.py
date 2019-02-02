from stock import stock, EnvironmentPrice, EnvironmentStock
from copy import deepcopy
import numpy as np

class Environment():
    def __init__(self):
        self.stock = deepcopy(EnvironmentStock)
        self.price = deepcopy(EnvironmentPrice)
        self.turnOver()

    def showEnvironmentStock(self):
        print("Environment stock")
        print(self.stock)
        print("")

    def sellStock(self,product,amount):
        self.stock[product] += amount
        return self.price[product]*amount

    def buyStock(self,product,amount):
        self.stock[product] -= amount
        return self.price[product]*amount

    def turnOver(self):
        for key in self.price.keys():
            self.price[key] = (0.997**self.stock[key])*10000
        print("price: ")
        print(self.price)
        print("")
