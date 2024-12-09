class Person:
    def __init__(self,PersonID,Name,Dob):
        self._PersonID = PersonID
        self._Name = Name
        self._Dob = Dob

    def __str__(self):
        return "ID: {}, Name: {}, Dob: {}".format(self._PersonID,self._Name,self._Dob)
    
    def input(self):
        self._PersonID = input("Enter ID: ")
        self._Name = input("Enter Name: ")
        self._Dob = input("Enter Dob: ")

    def list(self):
        return str(self)
    
class Student(Person):
    def __init__(self,StudentID,StudentName,Dob):
        super().__init__(StudentID,StudentName,Dob)
        self.__mark = {} #Dùng dictionary

    def inputMark(self,CourseID,mark):
        self.__mark[CourseID] = mark

    def listMark(self):
        return super().__str__() + "Marks: {}".format(self.__mark)
    
class Course:
    def __init__(self,CourseID,CourseName):
        self._CourseID = CourseID
        self._CourseName = CourseName

    def __str__(self):
        return "CourseID: {}, CourseName: {}".format(self._CourseID,self._CourseName)
    
    def input(self):
        self._CourseID = input("Enter Course ID: ")
        self._CourseName = input("Enter name of Course: ")

    def list(self):
        return str(self)
    
class StudentManagement:
    def __init__(self):
        self.__students = [] #Khai báo list
        self.__courses = []
        
    def addStudent(self):
        num_students = int(input("Enter the number of students to add: "))
        for i in range(num_students):
            student = Student("", "", "")
            student.input()  # Polymorphic
            self.__students.append(student)  # Thêm student vào list
        print(f"{num_students} students have been added.")

    def addCourse(self):
        num_courses = int(input("Enter the number of courses to add: "))
        for i in range(num_courses):
            course = Course("", "")
            course.input()
            self.__courses.append(course)  # Thêm course vào list
        print(f"{num_courses} courses have been added.")


    def inputMark(self):
        if not self.__students:
            print("No students available. Please add students first.")
            return
        
        if not self.__courses:
            print("No courses available. Please add courses first.")
            return
        
        CourseID = input("Input Course ID for which you want to enter the marks: ")
        #Check CourseID exists or not
        exist = False
        for course in self.__courses:
            if course._CourseID == CourseID:
                exist = True
                break
        
        if not exist:
            print("Can not find Course")
            return
        
        
        for student in self.__students:
            mark = float(input("Enter mark for Student: {} , ID: {}: ".format(student._Name,student._PersonID)))
            student.inputMark(CourseID,mark)

    def listStudent(self):
        if not self.__students:
            print("No students available!")
        else:
            print("\nList of Students:")
            for student in self.__students:
                print(student.list())  # Polymorphic 
    
    def listCourse(self):
        if not self.__courses:
            print("No courses available!")
        else:
            print("\nList of Courses:")
            for course in self.__courses:
                print(course.list())  
    
    def showMarks(self):
        if not self.__students:
            print("No students available. Please add students first.")
            return
        
        if not self.__courses:
            print("No courses available. Please add courses first.")
            return
        
        CourseID = input("Enter Course ID to show Mark: ")
        exist = False
        for course in self.__courses:
            if course._CourseID == CourseID:
                exist = True
                break
        
        if not exist:
            print("Can not find Course")
            return
        
        print("Mark for Course ID: {CourseID}")
        for student in self.__students:
            mark = student.listMark()
            if CourseID in mark:
                print("Student: {}, ID: {},mark: {}: ".format(student._Name,student._PersonID, mark))
            else :
                print("Student: {}, ID: {}, Mark: Not entered".format(student._Name, student._PersonID))
    
    def menu(self):
        while True:
            print("1.Input Number and Information of Student")
            print("2.Input Number and Information of Course")
            print("3.Input Mark for Course")
            print("4.List of Courses")
            print("5.List of Students")
            print("6.Show the Mark")
            print("7.Exit")

            choice = input("Choose an option (1-7): ")
            if choice == "1":
                self.addStudent()
            elif choice == "2":
                self.addCourse()
            elif choice == "3":
                self.inputMark()
            elif choice == "4":
                self.listStudent()
            elif choice == "5":
                self.listCourse()
            elif choice == "6":
                self.showMarks()
            elif choice == "7":
                print("Exit")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manage = StudentManagement()
    manage.menu()