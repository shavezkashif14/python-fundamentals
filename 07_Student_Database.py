students = {
    "Shavez": {
        "age": 17,
        "grade": "A*",
        "subject": "Computer Science"
    },
    "Ali": {
        "age": 16,
        "grade": "A",
        "subject": "Mathematics"
    },
    "Ahmed": {
        "age": 17,
        "grade": "B",
        "subject": "Physics"
    }
}

while True:
    print()
    print("1. View students")
    print("2. Add student")
    print("3. Search for student")
    print("4. Update grade")
    print("5. Exit")

    task = int(input("Choose an option: "))

    if task == 1:
        for name, information in students.items():
            print()
            print(name)
            print(f"Age: {information['age']}")
            print(f"Grade: {information['grade']}")
            print(f"Subject: {information['subject']}")

    elif task == 2:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        subject = input("Enter student subject: ")

        students[name] = {
            "age": age,
            "grade": grade,
            "subject": subject
        }

        print("Student added!")

    elif task == 3:
        name = input("Enter student name: ")

        if name in students:
            print(f"Name: {name}")
            print(f"Age: {students[name]['age']}")
            print(f"Grade: {students[name]['grade']}")
            print(f"Subject: {students[name]['subject']}")
        else:
            print("Student not found!")

    elif task == 4:
        name = input("Enter student name: ")

        if name in students:
            grade = input("Enter new grade: ")
            students[name]["grade"] = grade
            print("Grade updated!")
        else:
            print("Student not found!")

    elif task == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid selection!")