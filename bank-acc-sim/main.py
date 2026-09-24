balance = 0
actions = []
while True:
    print("--- BANK ---\n")
    menu = input("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. View Transaction History\n5. Exit\n:")
    if menu == "1":
        print(f"\nBalance: ${balance:.2f}\n")
    elif menu == "2":
        deposit = input("\nHow much would you like to deposit: $")
        deposit = float(deposit)
        if deposit <= 0:
            print("You cant deposit NOTHING!\n")
        else:
            balance += deposit
            print(f"You have deposited ${deposit:.2f}\n")
            action = {
                "transaction" : "Deposited",
                "amount": deposit
            }
            actions.append(action)
    elif menu == "3":
        withdraw = input("\nHow much would you like to withdraw: $")
        withdraw = float(withdraw)
        if withdraw <= 0:
                    print("You cant withdraw NOTHING!\n")
        elif withdraw > balance:
            print(f"You do not have enough money to withdraw ${withdraw:.2f}!\n")
        else:
            balance -= withdraw
            print(f"You have withdrawed ${withdraw:.2f}\n")
            action = {
                        "transaction" : "Withdrawed",
                        "amount": withdraw
                    }
            actions.append(action)
    elif menu == "4":
        if not actions:
            print("\nYou have made no transactions\n!")
        else:
            print("\n--- Transactions ---")
            for action in actions:
                print(f"{action['transaction']}: ${action['amount']:.2f}")
            print("--------------------\n")
    elif menu == "5":
        break
print("Goodbye!")