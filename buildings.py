from environnement import Environnement
from random import randint, choice
import yaml

Environnement = Environnement()

class BuildingProcess():

    def buyProduce(self,credit):
        for x in range (len(self.consumtion)):
            if (Environnement.stock[self.consumtion[x]] > 0):
                credit -= Environnement.buyStock(self.consumtion[x],self.consumtion_amount[x])
            else:
                credit -= 2000
        return credit

    def sellProduce(self,credit):
        credit += Environnement.sellStock(self.product,self.product_amount)
        return credit

    def turnOver(self):
        Environnement.turnOver()

    def showEnv(self):
        Environnement.showEnvironnementStock()
        Environnement.showEnvironnementPrice()


class Building(BuildingProcess):
    def __init__(self):
        self.product = []
        self.product_amount = []
        self.consumtion = []
        self.consumtion_amount = []
        self.setup()

    def setup(self):
        with open("config/production.yml", 'r') as stream:
            data_loaded = yaml.safe_load(stream)

        del data_loaded["Credits"]

        items = []
        for key in data_loaded.keys():
            items.append(key)

        material = choice(items)
        
        self.product = material
        self.product_amount = data_loaded[material]["Production"]
        for key in data_loaded[material]["Consumtion"].keys():
            self.consumtion.append(key)
            self.consumtion_amount.append(data_loaded[material]["Consumtion"][key])

    def showProductAndConsumtion(self):
        print("product: {}".format(self.product))
        print("consumtion: {}".format(self.consumtion))

if __name__ == "__main__":
    Environnement.showEnvironnementPrice()
    Environnement.showEnvironnementStock()
    building = Building()
    building.showProductAndConsumtion()
    credit = 100
    credit = building.buyProduce(credit)
    print("credit: {}".format(credit))