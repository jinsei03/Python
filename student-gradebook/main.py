students = []
while True:
    choice = input("1. Add Student and Grades\n2. View all students\n3. Determine letter grade of student\n4. Quit\n: ")
    if choice == "1":
        name = input("What is the Student's name: ")
        grades = input("Enter grades separated by spaces: ")
        grades = grades.split()
        for index, grade in enumerate(grades):
            grades[index] = int(grade)
        student_data = {
            "Name": name,
            "Grades": grades
        }
        students.append(student_data)
        print(students)
    elif choice == "2" and students:
        for student in students:
            print("Name: ", student["Name"])
            print("Grades:", *student["Grades"])
    elif choice == "3" and students:
        for student in students:
            grade =  sum(student["Grades"]) / len(student["Grades"])
            if grade >= 90:
                print(student["Name"],"has a A")
            elif grade <= 89 and grade >= 80:
                print(student["Name"], "has a B")
            elif grade <= 79 and grade >= 70:
                print(student["Name"], "has a C")
            elif grade <= 69 and grade >= 60:
                print(student["Name"], "has a D")
            else:
                print(student["Name"], "has a F")
    elif choice == "4":
        break
    elif not students:
        print("THERE ARE NO STUDENTS!!!")
    else:
        print("Please choose an option between 1-4.")

print("Good bye!")