students = []
while True:
    choice = input("1. Add Student and Grades\n2. View all students\n3. Determine letter grade of student\n4. Quit\n: ")
    if choice == "1":
        name = input("What is the Student's name: ")
        grade1 = input("What is the students 1st grade: ")
        grade2 = input("What is the students 2nd grade: ")
        grade3 = input("What is the students 3rd grade: ")
        student_data = {
            "Name": name,
            "Grade1": grade1,
            "Grade2": grade2,
            "Grade3": grade3
        }
        students.append(student_data)
        print(students)
    elif choice == "2":
        for student in students:
            print("Name: ", student["Name"])
            print("Grades:",student["Grade1"],",",student["Grade2"],",",student["Grade3"])
    elif choice == "3":
        for student in students:
            grade = (int(student["Grade1"]) + int(student["Grade2"]) + int(student["Grade3"])) / 3
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
print("Good bye!")