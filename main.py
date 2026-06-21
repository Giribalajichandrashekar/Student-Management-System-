import json

students = []


# =========================
# File Handling Functions
# =========================

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []

    except json.JSONDecodeError:
        students = []


# =========================
# Menu
# =========================

def menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


# =========================
# Add Student
# =========================

def add_student():
    student_id = input("Enter ID: ")

    # Prevent duplicate IDs
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    save_students()

    print("Student Added Successfully!")


# =========================
# View Students
# =========================

def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("\n----------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


# =========================
# Search Student
# =========================

def search_student():
    search_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found.")


# =========================
# Update Student
# =========================

def update_student():
    update_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == update_id:

            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            save_students()

            print("Student Updated Successfully!")
            return

    print("Student not found.")


# =========================
# Delete Student
# =========================

def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)

            save_students()

            print("Student Deleted Successfully!")
            return

    print("Student not found.")


# =========================
# Program Start
# =========================

load_students()

# =========================
# Main Loop
# =========================

while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Exiting...")
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid Choice. Please try again.")