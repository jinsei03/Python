print(f"==== Expense Tracker ====")
choice = input(f"1. View expenses\n2. Add expense\n3. View total\n4. Quit\n\nChoose an option: ")

expenses = []

while choice != "4":
    if choice == "1":
        if not expenses:
            print(f"You have no expenses!")
        for expense in expenses:
            print(f"{expense["category"]}: ${expense["amount"]:.2f}")
    elif choice == "2":
        category = input(f"Category: ")
        while not category:
            category = input(f"Please type a category: ")
        amount = input(f"Amount: $")
        while True:
            try: 
                amount = float(amount)
                break
            except ValueError:
                amount = input(f"Please enter a number: $")
        add = {
            "category": category, 
            "amount": amount
        }
        expenses.append(add)
    elif choice == "3":
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
        print(f"Total: ${total:.2f}")
    print(f"\n==== Expense Tracker ====")
    choice = input(f"1. View expenses\n2. Add expense\n3. View total\n4. Quit\n\nChoose an option: ")