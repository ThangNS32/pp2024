from domains.management import StudentManagement
from input import get_string_input, get_int_input, get_float_input


def menu():
    manager = StudentManagement()

    manager.loadData()

    while True:
        print("\n1. Input Number and Information of Students")
        print("2. Input Number and Information of Courses")
        print("3. Input Marks for Course")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Students Sorted by GPA")
        print("7. Save and Exit")

        choice = get_string_input("Choose an option (1-7): ")
        if choice == "1":
            manager.addStudent(get_string_input)
        elif choice == "2":
            manager.addCourse(get_string_input, get_int_input)
        elif choice == "3":
            manager.inputMark(get_float_input)
        elif choice == "4":
            manager.listStudent()
        elif choice == "5":
            manager.listCourses()
        elif choice == "6":
            manager.sortStudentByGPA()
        elif choice == "7":
            manager.saveData()
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()

