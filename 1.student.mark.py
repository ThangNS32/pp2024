# Danh sách lưu trữ students, courses , marks
students = [] 
courses = [] 
marks = []

# Input number and information: id, name, DoB of students in a class
def input_students():
    num_students = int(input("Input number of students: "))
    for i in range(num_students):
        # Input information of students
        studentID = input("Input the Student id: ")
        studentName = input("Input name of Student: ")
        dob = input("Input DoB(dd/mm/yyyy): ")
        # Add info to the LIST students
        students.append({"Student ID": studentID , "Name": studentName ,"DoB":dob})


# Input number of courses and information of courses
def input_courses():
    num_courses = int(input("Input number of courses: "))
    for i in range(num_courses):
        courseID = input("Input the Course ID: ")
        courseName = input("Input Name of Course: ")

        courses.append({"Course ID": courseID,"Course Name": courseName })

# Input marks for student in this course
def input_marks():
    if not students:
        print("List of student is empty! Let input info of student")
        input_students()

    if not courses:
        print("List of course is empty! Let input info of course")
        input_courses()
    

    courseID = input("Input Course ID for which you want to enter the marks: ")
    # Check Course ID exist or not
    exist = False
    for course in courses:
        if course["Course ID"] == courseID :
            exist = True
            break
    if not exist: 
        print("Can not find Course ID")

    for student in students:
        mark = float(input("Enter the Mark for Student {} (ID: {}): " .format(student["Name"] , student["Student ID"])))
        marks.append({"Student ID": student["Student ID"] , "Course ID": courseID, "Mark":mark })


# List Courses
def list_courses():
    if not courses:
        print("List of course is empty! Let input info of course")
        input_courses()

    print("\nList of Course: ")
    for course in courses:
        print("Course ID: {0} , Course Name {1}".format(course["Course ID"] , course["Course Name"]))

# List Students
def list_students():
    if not students:
        print("List of student is empty! Let input info of student")
        input_students()
        

    print("\nList of Students: ")
    for student in students:
        print("Student ID: {0} ,Student Name {1} ,DoB: {2}".format(student["Student ID"], student["Name"], student["DoB"]))

# Show Mark
def show_marks():
    if not students:
        print("List of student is empty! Let input info of student")
        input_students()

    if not courses:
        print("List of course is empty! Let input info of course")
        input_courses()

    if not marks:
        print("Mark of Student is empty! Let input Mark")
        input_marks()

    courseID = input("Input Course ID to show marks: ")
    exist = False
    for course in courses:
        if course["Course ID"] == courseID:
            exist = True
            break
    if not exist:
        print("Can not find Course ID")
    
    print("\nMark of Student for Course {0}: ".format(courseID))
    for mark in marks:
        if mark["Course ID"] == courseID :
            # Get student name based on ID
            studentName = next(student["Name"] for student in students if (student["Student ID"] == mark["Student ID"]))
            print("Student {} , Mark {}".format(studentName , mark["Mark"]))

def main():
    while True:
        print("1.Input Number and Information of Student")
        print("2.Input Number and Information of Course")
        print("3.Input Mark for Course")
        print("4.List of Courses")
        print("5.List of Students")
        print("6.Show the Mark")
        print("7.Exit")

        choice = input("Choose any number (1 - 7 ): ")
        if choice == "1" :
            input_students()
        elif choice == "2" :
            input_courses()
        elif choice == "3" :
            input_marks()
        elif choice == "4" :
            list_courses()
        elif choice == "5" :
            list_students()
        elif choice == "6" :
            show_marks()
        elif choice == "7" :
            print("Exit.")
            break
        else:
            print("Invalid input. Try again")
    

if __name__ == "__main__":
    main()

