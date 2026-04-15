
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append(
{'amount': amount,'description': description})

    def withdraw(self, amount,description=""):

        if self.check_funds(amount):
            self.ledger.append(
{'amount': -amount,'description': description})
            return True

        return False

    def get_balance(self):
        total = 0 
        for obj in self.ledger :
            total += obj['amount']
        return total 

    def transfer(self, amount, Destination):

        if self.check_funds(amount):

            self.withdraw(amount,f"Transfer to {Destination.name}")

            Destination.deposit(amount,f"Transfer from {self.name}")

            return True
        
        return False
    
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True

    def __str__(self):

        output = self.name.center(30, "*") + "\n"
        for item in self.ledger :
            output += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    text = "Percentage spent by category\n"
    
    withdrawals = []

    for category in categories:
        withdrawal = 0
        for item in category.ledger:
            withdrawal += -item['amount'] if item['amount'] < 0 else 0
        withdrawals.append(withdrawal)
    
    total = sum(withdrawals)

    percentages = [int(w / total*10)*10  for w in withdrawals]

    for i in range(100, -1, -10):
        text += f"{i:>3}| "
        for percentage in percentages:
            text += "o  " if percentage >= i else "   "
        text += "\n"  

    text += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)

    for i in range(max_len):
        text += "     "   # 5 spaces

        for category in categories:
            if i < len(category.name):
                text += category.name[i] + "  "
            else:
                text += "   "

        if i < max_len - 1:
            text += "\n"

    return text



