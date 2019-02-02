from business import Business

class Top():
    def __init__(self):
        self.companies = [Business()]

    def showCompanyStocks(self):
        for company in self.companies:
            company.showStock()

    def showCompanyHoldings(self):
        for company in self.companies:
            company.showHoldings()

    def turnOver(self):
        for company in self.companies:
            company.turnOver()

test = Top()

print("company stocks:")
test.showCompanyStocks()
print("")
print("company Holdings:")
test.showCompanyHoldings()
print("")
print("")

for x in range (10):
    test.turnOver()

    print("company stocks:")
    test.showCompanyStocks()
    print("")
    print("company Holdings:")
    test.showCompanyHoldings()
    print("")
    print("")
