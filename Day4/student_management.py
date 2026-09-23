import json


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }


students = []

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Students saved.")


def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")

    try:
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))

        if age <= 0:
            print("Age must be greater than 0.")
            return

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        student = Student(name, age, marks)
        students.append(student)

        print("Student added successfully.")

    except ValueError:
        print("Please enter valid numbers for age and marks.")


def view_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No students found.")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print(f"Name   : {student.name}")
        print(f"Age    : {student.age}")
        print(f"Marks  : {student.marks}")


def search_student():
    print("\n--- Search Student ---")

    search_name = input("Enter student name: ").lower()

    found = False

    for student in students:
        if student.name.lower() == search_name:
            print("\nStudent Found")
            print(f"Name  : {student.name}")
            print(f"Age   : {student.age}")
            print(f"Marks : {student.marks}")

            found = True
            break

    if not found:
        print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    delete_name = input("Enter student name: ").lower()

    for student in students:
        if student.name.lower() == delete_name:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def save_students():
    data = []

    for student in students:
        data.append(student.to_dict())

    try:
        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Students saved successfully.")

    except Exception as e:
        print("Error while saving students:", e)


def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            data = json.load(file)

        students = []

        for student_data in data:
            student = Student(
                student_data["name"],
                student_data["age"],
                student_data["marks"]
            )

            students.append(student)

        print("Students loaded successfully.")

    except FileNotFoundError:
        print("No previous student data found.")

    except Exception as e:
        print("Error while loading students:", e)


def show_menu():
    print("\n================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Students")
    print("6. Exit")
    print("================================")


def main():
    load_students()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            save_students()

        elif choice == "6":
            save_students()
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()