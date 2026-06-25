import json

students = []


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


def menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add Marks")
    print("7. update marks")
    print("8. View results")
    print("9. Exit")




def add_student():
    student_id = input("Enter ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    while True:
        name = input("Enter Name: ").strip()

        if name == "":
            print("Name cannot be empty.")
        else:
            break

    while True:
        age = input("Enter Age: ").strip()
        
        if age.isdigit():
            if 1<= int(age) <= 120:
                break
            else:
                print("Age must be between 1 and 120.")
        else:
            print("Enter a valid number for age.")

    while True:
        course = input("Enter Course: ").strip()
        if course == "":
            print("Course cannot be empty.")
        else:
            break


    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    save_students()

    print("Student Added Successfully!")



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



def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)

            save_students()

            print("Student Deleted Successfully!")
            return

    print("Student not found.")

def get_marks(subject):

    while True:
        marks = input(f"Enter {subject} Marks: ")

        if marks.isdigit():

            marks = int(marks)

            if 0 <= marks <= 100:
                return marks

            else:
                print("Marks must be between 0 and 100.")

        else:
            print("Please enter a valid number.")

def add_marks():

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            # Check if marks already exist
            if "maths" in student:

                print("Marks already exist.")
                print("Use Update Marks instead.")
                return

            maths = get_marks("Maths")
            english = get_marks("English")
            science = get_marks("Science")

            student["maths"] = maths
            student["english"] = english
            student["science"] = science

            save_students()

            print("Marks Added Successfully!")
            return

    print("Student not found.")

def calculate_grade(average):

    if average >= 90:
        return "A"

    elif average >= 75:
        return "B"

    elif average >= 60:
        return "C"

    else:
        return "F"

def update_marks():

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            if "maths" not in student:

                print("Marks not found.")
                print("Use Add Marks first.")
                return

            print("\nCurrent Marks")
            print("Maths:", student["maths"])
            print("English:", student["english"])
            print("Science:", student["science"])

            print("\nEnter New Marks")

            student["maths"] = get_marks("Maths")
            student["english"] = get_marks("English")
            student["science"] = get_marks("Science")

            save_students()

            print("Marks Updated Successfully!")
            return

    print("Student not found.")

    
def view_result():

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            if "maths" not in student:

                print("Marks not available.")
                return

            total = (
                student["maths"]
                + student["english"]
                + student["science"]
            )

            average = total / 3

            grade = calculate_grade(average)

            print("\n===== RESULT =====")
            print("ID:", student["id"])
            print("Name:", student["name"])

            print("\nMaths:", student["maths"])
            print("English:", student["english"])
            print("Science:", student["science"])

            print("\nTotal:", total)
            print("Average:", round(average, 2))
            print("Grade:", grade)

            return

    print("Student not found.")


load_students()


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
        add_marks()

    elif choice == "7":
        update_marks()

    elif choice == "8":
        view_result()

    elif choice == "9": 
        print("Exiting...")
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid Choice. Please try again.")