print(f"==== TO DO LIST ====\n")

tasks = []

choice = input(f"1. View Tasks\n2. Add Task\n3. Remove Task\n4. Quit\n\nChoose an option: ")

while choice != "4":

    if choice == "1":
        print(f"==== TASKS ====")
        if not tasks:
            print("You have no tasks!\n")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")

    elif choice == "2":
        add = input(f"Enter a task: ")
        while not add:
            add = input(f"Please type a Task!: ")
        tasks.append(add)
        print(f"Task added!\n\n")
        print(tasks)

    elif choice == "3":
        if not tasks:
            print("You have not tasks!\n")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            remove = input(f"Remove Task #: ")
            while True:
                try:
                    valid_int = int(remove) - 1                    
                    while valid_int > index or valid_int < 0:
                        remove = input(f"That task does not exist. Please try again: ")
                        valid_int = int(remove) - 1
                    break
                except ValueError:
                    remove = input(f"Please enter a number: ")
            removed = tasks.pop(int(remove) - 1)
            print(f"Removed: {removed}\n\n")

    print(f"==== TO DO LIST ====\n")
    choice = input(f"1. View Tasks\n2. Add Task\n3. Remove Task\n4. Quit\n\nChoose an option: ")

print(f"Goodbye!")