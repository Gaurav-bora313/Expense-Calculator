#expense tracker

while True:
    expense_type = ("food", "transportation", "utilities", "entertainment", "others")
    expenditure = {}
    total = 0
    for type in expense_type:
        amount = float(input(f"Enter your {type} expense: "))
        expenditure[type] = amount   
    print("---------------EXPENDITURE---------------")
    for expense_type, cost in expenditure.items():
        print(f"{expense_type}: ${cost:.2f}")
        total += cost
    print("-----------------------------------------")
    print("TOTAL: $", total)
    break