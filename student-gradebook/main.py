students = []
choice = input("1. Add Student and Grades\n2. View all students\n3. Determine letter grade of student\n4. Quit\n: ")
while choice != "4":
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
    elif choice == "2":
        for sutdent_data in students:
            print("Name: ", student_data["Name"])
            print("Grades:",student_data["Grade1"],",",student_data["Grade2"],",",student_data["Grade3"])
    elif choice == "3":
        for student_data in students:
            grade = (int(student_data["Grade1"]) + int(student_data["Grade2"]) + int(student_data["Grade3"])) / 3
            if grade >= 90:
                print(student_data["Name"],"has a A")
            elif grade <= 89 and grade >= 80:
                print(student_data["Name"], "has a B")
            elif grade <= 79 and grade >= 70:
                print(student_data["Name"], "has a C")
            elif grade <= 69 and grade >= 60:
                print(student_data["Name"], "has a D")
            else:
                print(student_data["Name"], "has a F")
                
    choice = input("\n1. Add Student and Grades\n2. View all students\n3. Determine letter grade of student\n4. Quit\n: ")
print("Good bye!")