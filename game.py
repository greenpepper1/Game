from business import Business

class Top():
    def __init__(self):
        self.companies = [Business(), Business()]

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

test.showCompanyStocks()
test.showCompanyHoldings()

for x in range (10):
    test.turnOver()

    test.showCompanyStocks()
    test.showCompanyHoldings()
