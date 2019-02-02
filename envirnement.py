from stock import stock, EnvironmentPrice, EnvironmentStock
from copy import deepcopy
import numpy as np

class Environment():
    def __init__(self):
        self.stock = deepcopy(EnvironmentStock)
        self.prevStock = deepcopy(EnvironmentStock)
        self.price = deepcopy(EnvironmentPrice)

    def showEnvironmentStock(self):
        print(self.stock)

    def sellStock(self,product,amount):
        self.stock[product] += amount
        return self.price[product]*amount

    def buyStock(self,product,amount):
        self.stock[product] -= amount
        return self.price[product]*amount

    # Needs a tidy and the price can go below zero

    def turnOver(self):
        pre = self.prevStock.values()
        cur = self.stock.values()
        change = [p - c for p, c in zip(pre,cur)]
        print (change)
        # adjust = self.softmax(self.stock.values())
        # top = max(adjust)
        # adjust = adjust - (top/2)
        # adjust = -adjust
        # print (adjust)
        # print (self.price)
        # x = 0
        # for key in self.price.keys():
        #     self.price[key] +=adjust[x]
        #     x = x +1
        # print (self.price)

    def softmax(self,x):
        """Compute softmax values for each sets of scores in x."""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0) # only difference
