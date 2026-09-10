
def printTasks(tasks):
    #Prints each task numerically line by line
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
    #returns the index so it can be used to manipulate the list
    return index

def menu():
    print(f"==== TO DO LIST ====\n")
    choice = input(f"1. View Tasks\n2. Add Task\n3. Remove Task\n4. Quit\n\nChoose an option: ")
    return choice

def testInput(remove, index):
    while True:
        try:
            valid_int = int(remove) - 1                    
            while valid_int > index or valid_int < 0:
                remove = input(f"That task does not exist. Please try again: ")
                valid_int = int(remove) - 1
            break
        except ValueError:
            remove = input(f"Please enter a number: ")
    return valid_int
        
tasks = []

choice = menu()

while choice != "4":
    
    if choice == "1":
        print(f"==== TASKS ====")
        if not tasks:
            print("You have no tasks!\n")
        else:
            printTasks(tasks)
            
    elif choice == "2":
        add = input(f"Enter a task: ")
        while not add:
            add = input(f"Please type a Task!: ")
        tasks.append(add)
        print(f"Task added!\n\n")

    elif choice == "3":
        if not tasks:
            print("You have not tasks!\n")
        else:
            index = printTasks(tasks)
            remove = input(f"Remove Task #: ")
            remove = testInput(remove, index)
            removed = tasks.pop(int(remove))
            print(f"Removed: {removed}\n\n")
    choice = menu()

print(f"Goodbye!")