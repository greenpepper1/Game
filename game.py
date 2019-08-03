from business import Business

class Top():
    def __init__(self):
        self.companies = [Business(),Business(),Business(),Business(),Business()]

    def showCompanyValue(self):
        for company in self.companies:
            company.showValue()

    def showCompanyHoldings(self):
        for company in self.companies:
            company.showHoldings()
            print("")

    def showEnv(self):
        self.companies[0].showEnv()

    def businessTurnOver(self):
        for company in self.companies:
            company.businessTurnOver()

    def envirenmentTurnOver(self):
        self.companies[0].envirenmentTurnOver()

test = Top()
test.showCompanyHoldings()
print("")
for x in range (10):
    test.showEnv()
    test.showCompanyValue()
    test.businessTurnOver()
    test.envirenmentTurnOver()
    print("")