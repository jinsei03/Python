library = []
while True:
    menu = input("\n--- LIBRARY ---\n1. Add Book\n2. View Books\n3. Borrow Book\n4. Return Book\n5. Exit\n:")
    if menu == "1":
        title = input("\nTitle: ")
        author = input("Author: ")
        book = {
            "Title": title,
            "Author": author,
            "Available": "Yes"
        }
        library.append(book)
    elif menu == "2":
        for book in library:
            print(f"\nTitle: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Available: {book['Available']}")
    elif menu == "3":
        borrow = input(f"\nWhich book would you like to borrow?: ")
        found = False
        for book in library:
            if book['Title'] == borrow and book['Available'] == "Yes":
                print(f"You have succesfully borrowed {book['Title']}!\n")
                book['Available'] = "No"
                found = True
                break
            elif book['Title'] == borrow and book['Available'] == "No":
                print(f"Unfortunatley {book['Title']} is being borrowed already!\n")
                found = True
                break
        if found != True:
            print("That book is not in this library!\n")
    elif menu == "4":
        returnBook = input(f"Which book would you like to return?: ")
        found = False
        for book in library:
            if book['Title'] == returnBook and book['Available'] == "Yes":
                print(f"You cant return {book['Title']} since its available!\n")
                found = True
                break
            elif book['Title'] == returnBook and book['Available'] == "No":
                print(f"You have sucessfully returned {book['Title']}!\n")
                book['Available'] = "Yes"
                found = True
                break
        if found != True:
            print("That book is not in this library!\n")
    elif menu == "5":
        print("Goodbye!")
        break