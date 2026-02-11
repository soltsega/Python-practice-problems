class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Header: centered name in 30 '*'
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            # Format description (23 chars) and amount (7 chars, 2 decimal places)
            desc = f"{entry['description'][:23]:23}"
            amt = f"{entry['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    # 1. Calculate spending per category and total spending
    spending = []
    for cat in categories:
        spent = sum(item['amount'] for item in cat.ledger if item['amount'] < 0)
        spending.append(abs(spent))
    
    total_spent = sum(spending)
    # Calculate percentages rounded down to the nearest 10
    # Guard against division by zero if no spending has occurred
    percentages = [int((s / total_spent * 100) // 10) * 10 if total_spent > 0 else 0 for s in spending]

    # 2. Build the top of the chart (the bars)
    res = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        res += f"{i:>3}| "
        for p in percentages:
            res += "o  " if p >= i else "   "
        res += "\n"

    # 3. Build the horizontal line
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 4. Build the vertical names
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]
    
    for i in range(max_len):
        res += "     "
        for name in names:
            res += name[i] + "  "
        if i < max_len - 1:
            res += "\n"

    return res