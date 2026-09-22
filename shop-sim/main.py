items=[]
money = 100.00

print(f"You have ${money:.2f}")

while True:
    menu = input("---- SHOP ----\n1. Add item\n2. View Shop\n3. Search Item\n4. Buy Item\n5. Exit\n: ")
    if menu == "5":
        break
    elif menu == "1":
        name = input("What is the name of the item: ")
        price = input("How much does it cost: $")
        quantity = input("How many are you adding: ")
        item = {
            "Name" : name,
            "Price" : float(price),
            "Quantity": int(quantity)
        }
        items.append(item)
        print(items)
    elif menu == "2":
        for item in items:
            print("\nName: ",item["Name"])
            print(f"Price: ${item['Price']:.2f}")
            print("Quantity: ",item["Quantity"],"\n")
    elif menu == "3":
        search = input("What are you looking for?: ")
        found = False
        for item in items:
            if item["Name"] == search:
                print("We have that in stock!")
                found = True
        if found == False:
            print("Sorry we don't have that")
    elif menu == "4":
        buy = input(f"You currently have {money:.2f} What are you buying?: ")
        found = False
        for item in items:
            if item["Name"] == buy:
                found = True
                if item["Price"] > money:
                    print("YOU DONT HAVE ENOUGH MONEY FOR THAT!")
                else:
                    print(f"The {item['Name']} is ${item['Price']:.2f}")
                    confirm = input("Would you like to purchase it (y/n): ")
                    if confirm == "y":
                        money -= item['Price']
                        item['Quantity'] -= 1
                        if item['Quantity'] == 0:
                            items.remove(item)
        if found == False:
            print("Sorry we don't have that")


