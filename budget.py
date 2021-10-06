def repeater(st, x):
    endstring = ""
    count = 0
    while count < x:
        endstring = endstring+st
        count += 1
    return endstring

class Category:
    ledger = list()
    name = str()

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description = ""):
        try:
            amount = float(amount)
        except:
            print('Not able to process float')
            return None
        lijstje = {"amount" : 0,
        "description": ""}
        lijstje['amount'] = amount
        lijstje['description'] = description
        self.ledger.append(lijstje)
        return None
    
    def get_balance(self):
        total = float()
        for bonnetje in self.ledger:
            total += bonnetje['amount']
        return round(total, 2)
    
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            amount = 0 - amount
            self.deposit(amount, description)
            return True
        else:
            return False
    
    def transfer(self, amount, othercat):
        if self.check_funds(amount):
            try:
                descriptionfrom = "Transfer from "+self.name
                othercat.deposit(amount, descriptionfrom)
                descriptionto = "Transfer to "+othercat.name
                self.withdraw(amount, descriptionto)
                return True
            except:
                return False
        else:
            return False

    def __str__(self):
        endstring = ""
        amount_of_stars = 30 - len(self.name)
        stars_left = amount_of_stars//2
        stars_right = 30 - stars_left - len(self.name)
        endstring = repeater("*", stars_left)+self.name+repeater("*", stars_right)+"\n"
        for bonnetje in self.ledger:
            dispstr = bonnetje['description'][:23]
            dispprice = "{:.2f}".format(round(bonnetje['amount'], 2))[:7]
            dispspace = 30 - len(dispstr) - len(dispprice)
            endstring = endstring+dispstr+repeater(" ", dispspace)+dispprice+"\n"
        endstring = endstring+"Total: "+str(self.get_balance())

        return endstring

def create_spend_chart(categories):
    spend_amount = list()
    for category in categories:
        catamount = 0.0
        bonnetjes = category.ledger
        for bonnetje in bonnetjes:
            if bonnetje['amount'] < 0:
                catamount += bonnetje['amount']
        spend_amount.append(catamount)
    totalspend = 0.0
    for amount in spend_amount:
        totalspend -= amount
    cat_percentage = list()
    for amount in spend_amount:
        cat_percentage.append((0-amount)/totalspend*100//10*10)

    endstring = "Percentage spent by category\n"
    percent = 100
    while percent >= 0:
        endstring = endstring+str(percent)+"|"
        for cat in cat_percentage:
            endstring = endstring+" "
            if cat >= percent:
                endstring = endstring+"o"
            else:
                endstring = endstring+" "
            endstring = endstring+" "
        endstring = endstring+" \n "
        percent -= 10
        if percent == 0:
            endstring = endstring+" "
    
    endstring = endstring+repeater(" ", 3)+repeater("-", len(spend_amount)*3+1)+"\n"
    nmls = list()
    for cat in categories:
        nmls.append(cat.name)

    longest_name = 0
    for name in nmls:
        if len(name) > longest_name:
            longest_name = len(name)
    
    count = 0
    while count < longest_name:
        endstring = endstring+"    "
        for name in nmls:
            endstring = endstring+" "
            if count < len(name):
                endstring = endstring+name[count]
            else:
                endstring = endstring+" "
            endstring = endstring+" "
        if count < longest_name -1:
            endstring = endstring+" \n"
        else:
            endstring = endstring+" "
        count += 1
    
    return endstring

food = Category("Food")
winkel = Category("Winkel")
auto = Category("Auto")
print(winkel.name)
print(food.name)
food.deposit(100.39, "salaris")
auto.deposit(500)
auto.withdraw(10)
print(food.transfer(30.61, winkel))
winkel.withdraw(20, 'test2')
winkel.withdraw(3, 'test3')
food.deposit(10, 'Tien euro er bij')
print(food)
