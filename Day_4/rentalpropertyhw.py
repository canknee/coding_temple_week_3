class ROIcalc:
    TAXPERCENT = {
        "Hawaii": 0.28, 
        "Alabama": 0.41,
        "Colorado": 0.51,
        "Louisiana": 0.55,
        "District of Columbia": 0.56,
        "South Carolina": 0.57,
        "Delaware": 0.57,
        "West Virginia": 0.58,
        "Nevada": 0.6,
        "Wyoming": 0.61,
        "Arkansas": 0.62,
        "Utah": 0.63,
        "Arizona": 0.66,
        "Idaho": 0.69,
        "Tennessee": 0.71,
        "California": 0.76,
        "New Mexico": 0.8,
        "Mississippi": 0.81,
        "Virginia": 0.82,
        "Montana": 0.84,
        "North Carolina": 0.84,
        "Indiana": 0.85,
        "Kentucky": 0.86,
        "Florida": 0.89,
        "Oklahoma": 0.9,
        "Georgia": 0.92,
        "Missouri": 0.97,
        "Oregon": 0.97,
        "North Dakota": 0.98,
        "Washington": 0.98,
        "Maryland": 1.09,
        "Minnesota": 1.12,
        "Alaska": 1.19,
        "Massachusetts": 1.23,
        "South Dakota": 1.31,
        "Maine": 1.36,
        "Kansas": 1.41,
        "Michigan": 1.54,
        "Ohio": 1.56,
        "Iowa": 1.57,
        "Pennsylvania": 1.58,
        "Rhode Island": 1.63,
        "New York": 1.72,
        "Nebraska": 1.73,
        "Texas": 1.80,
        "Wisconsin": 1.85,
        "Vermont": 1.9,
        "Connecticut": 2.14,
        "New Hampshire": 2.18,
        "Illinois": 2.27,
        "New Jersey": 2.49,
    }

    INSURANCE = 0.01

    def __init__(self, units):
        self.units = units

    def incomes(self): # Function for determining income per unit
        incomelist = []
        n = int(input("Enter how many sources of income you have followed by the monetary value of each source: "))
        for i in range(0, n):
            num = int(input())
            incomelist.append(num)
        print(f"You will receive a total of ${sum(incomelist) * self.units} per month")
        return sum(incomelist) * self.units

    def findStatePTax(self):
        condition = True
        while condition:
            state = input("What state is the property in? ").title()
            if state in ROIcalc.TAXPERCENT:
                print(f"The property tax in {state} is {ROIcalc.TAXPERCENT[state]}%")
                return ROIcalc.TAXPERCENT[state] / 100
            else:
                print("Enter a valid state")
            
    def calcStatePTax(self):
        propertycost = int(input("Input the cost of the property: "))
        ptax = round((propertycost * self.findStatePTax()), 2)
        print(f"You will be paying ${ptax} a year")
        return ptax
    
    def expenses(self): # Function for determining expense per unit
        expenselist = []
        n = int(input("Enter how many expenses you have followed by the monetary value of each expense: "))
        for i in range(0, n):
            num = int(input())
            expenselist.append(num)
        print(f"You will expend a total of ${sum(expenselist) * self.units} per month")
        return sum(expenselist) * self.units
    
    def insurance(self):
        propertycost = int(input("Input the cost of the property "))
        insurance = float(propertycost * ROIcalc.INSURANCE)
        print(f"You will be paying ${insurance} a year")
        return insurance

    def cashFlow(self):
        monthlycashflow = self.incomes() - self.expenses()
        print(f"You will be profiting ${monthlycashflow} a month")
        return monthlycashflow

    def investment(self):
        downpayment = int(input("Enter the downpayment: "))
        closingcosts = int(input("Enter any closing costs: "))
        repairs = int(input("Enter any repairs or rehabs needed: "))
        other = int(input("Enter any other expenditures made on inital investment. Enter 0 for none "))
        print(f"Your initial investment cost totals ${downpayment + closingcosts + repairs + other}")
        return (downpayment + closingcosts + repairs + other)

    def roi(self):
        ROI = (self.cashFlow()*12) / self.investment() 
        print(f"Your annual ROI is {ROI * 100}%")
        return ROI

test = ROIcalc(1)
test.roi()