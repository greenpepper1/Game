from buildings import Building
from random import randint, choice

class Business():
    def __init__(self):
        self.holdings = [Building(),Building()]
        self.credit = 100
        self.currentShare = int(self.credit/1000)
        self.actShare = int(self.credit/1000)

    def showHoldings(self):
        for hold in self.holdings:
            print("comp product: {}".format(hold.product))

    def showEnv(self):
        self.holdings[0].showEnv()
    
    def showValue(self):
        print("credit: {}".format(self.credit))
        print("actShare: {}".format(self.actShare))
        print("currentShare: {}".format(self.currentShare))

    def businessTurnOver(self):
        for hold in self.holdings:
            self.credit = hold.sellProduce(self.credit)
            self.credit = hold.buyProduce(self.credit)

        if (self.credit > 5000):
            self.holdings.append(Building())
            print("new building: {}".format(self.holdings[-1].product))
            self.credit -= 5000
        self.actShare = int((self.credit + (len(self.holdings)-2) * 5000)/100)
        self.currentShare = int((self.actShare - self.currentShare) /2)

    def envirenmentTurnOver(self):
        self.holdings[0].turnOver()

if __name__ == "__main__":