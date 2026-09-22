items=[]

while True:
    menu = input("---- SHOP ----\n1. Add item\n2. View inventory\n3. Search Item\n4. Buy Item\n5. Inventory Value\n6. Exit\n: ")
    if menu == "6":
        break
    elif menu == "1":
        name = input("What is the name of the item: ")
        price = input("How much does it cost: ")
        quantity = input("How many are you adding: ")
        item = {
            "Name" : name,
            "Price" : price,
            "Quantity": quantity
        }
        items.append(item)
        print(items)