import json

with open("contacts.JSON", "r") as file:
    contacts = json.load(file)
print(contacts)

while True:
    print(f"Contact Book\n")
    menu = input(
        "1. Add a contact\n"
        "2. View Contacts\n"
        "3. Search contacts\n"
        "4. Remove Contact\n"
        "5. Exit\n:"
    )

    if menu == "1":
        name = input(f"What is the contact's name: ")
        phone = input(f"What is the contact's phone number: ")
        email = input(f"What is the contact's email: ")
        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email
        }
        contacts.append(contact)
    elif menu == "2":
        for contact in contacts:
            print("Name:",contact["Name"])
            print("Phone:",contact["Phone"])
            print("Email:",contact["Email"])
    elif menu == "3":
        search = input(f"Type the name, phone number, or email: ")
        found = False
        for contact in contacts:
            if search == contact["Name"] or search == contact["Phone"] or search == contact["Email"]:
                print("Name:",contact["Name"])
                print("Phone:",contact["Phone"])
                print("Email:",contact["Email"])
                found = True
                break
        if not found:
            print("Contact not found!")
    elif menu == "4":
        remove = input(f"Whose contact would you like to remove: ")
        found = False
        for contact in contacts:
            if remove == contact["Name"] or remove == contact["Phone"] or remove == contact["Email"]:
                contacts.pop(contacts.index(contact))
                found = True
                print("Contact removed!")
                break
        if not found:
            print("Contact not found!")

    elif menu == "5":
        break

with open("contacts.JSON", "w") as file:
    json.dump(contacts, file, indent=4)

