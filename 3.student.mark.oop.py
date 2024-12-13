import numpy as np
import math

class Person:
    def __init__(self,PersonID,Name,Dob):
        self._PersonID = PersonID 
        self._Name = Name
        self._Dob = Dob

    def __str__(self):
        return "ID: {} ,Name: {}, DoB: {}".format(self._PersonID,self._Name,self._Dob)
    
    def input(self):
        self._PersonID = input("Enter ID: ")
        self._Name = input("Enter name: ")
        self._Dob = input("Enter Dob: ")

    def list(self):
        return str(self)
    
class Student(Person):
    def __init__(self,StudentID,StudentName,Dob):
        super().__init__(StudentID,StudentName,Dob)
        self.__marks = {} #dict
        self.__gpa = 0

    def inputMark(self,CourseID,mark):
        round_DownMark = math.floor(mark * 10) / 10 #to round-down student scores to 1-digit decimal
        self.__marks[CourseID] = round_DownMark #Add Round Down Mark to dict Mark

    def listMark(self):
        return super().__str__() + ", Mark: {}".format(self.__marks) 
    
    def calculateGPA(self , TinChi):
        tongDiem = sum(self.__marks[course] * TinChi[course] for course in self.__marks )
        tongTinChi = sum(TinChi[course] for course in self.__marks)
        if (tongTinChi > 0):
            self.__gpa = tongDiem / tongTinChi
        else: 
            self.__gpa = 0

        return self.__gpa
    
    def getGPA(self):
        return self.__gpa
    
class Course:
    def __init__(self,CourseID,CourseName ,TinChi):
        self._CourseID = CourseID
        self._CourseName = CourseName
        self._TinChi = TinChi

    def __str__(self):
        return "CourseID: {}, CourseName: {}".format(self._CourseID,self._CourseName)
    
    def input(self):
        self._CourseID = input("Enter Course ID: ")
        self._CourseName = input("Enter Course Name: ")
        self._TinChi = int(input("Enter Credits for the Course: "))

    def list(self):
        return str(self)
    
class StudentManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__TinChis = {}

    def addStudent(self):
        num_students = int(input("Enter the number of student to add: "))
        for i in range (num_students):
            student = Student("","","")
            student.input()
            self.__students.append(student)
        print(f"{num_students} student have been added.")

    def addCourse(self):
        num_course = int(input("Enter the number of Course to add: "))
        for i in range(num_course):
            course = Course("","","")
            course.input()
            self.__courses.append(course)
            self.__TinChis[course._CourseID] = course._TinChi
        print(f"{num_course} course have been added")

    def inputMark(self):
        if not self.__students:
            print("No students available. Please add students first.")
            return
        
        if not self.__courses:
            print("No courses available. Please add courses first.")
            return
        
        CourseID = input("Input Course ID for which you want to enter the marks: ")
        if CourseID not in self.__TinChis:
            print("Can not find Course")
            return
        
        for student in self.__students:
            mark = float(input("Enter mark for Student: {}, ID: {}: ".format(student._Name,student._PersonID)))
            student.inputMark(CourseID,mark)

    def calculateAllGPA(self):
        for student in self.__students:
            student.calculateGPA(self.__TinChis)

    def listStudent(self):
        if not self.__students:
            print("No students available!")
        else:
            print("\nList of Students:")
            for student in self.__students:
                print(student.list())  # Polymorphic 

    def listCourses(self):
        if not self.__courses:
            print("No courses available!")
        else:
            print("\nList of Courses:")
            for course in self.__courses:
                print(course.list())

    def sortStudentByGPA(self):
        self.calculateAllGPA()

        # Get GPA array from students
        gpa_array = np.array([student.getGPA() for student in self.__students])
        #Sort by GPA
        sortStudent = np.argsort(-gpa_array) #Follow decreasing
        #print dict Student
        print("\nStudent sorted by GPA (decreasing): ")
        for i in sortStudent:
            student = self.__students[i]
            print("Student {}, GPA: {}".format(student._Name,student.getGPA()))

    def menu(self):
        while (True):
            print("\n1. Input Number and Information of Students")
            print("2. Input Number and Information of Courses")
            print("3. Input Marks for Course")
            print("4. List Courses")
            print("5. List Students")
            print("6. Show Students Sorted by GPA")
            print("7. Exit")

            choice = input("Choose an option (1-7): ")
            if choice == "1" :
                self.addStudent()
            elif choice == "2":
                self.addCourse()
            elif choice == "3":
                self.inputMark()
            elif choice == "4":
                self.listCourses()
            elif choice == "5":
                self.listStudent()
            elif choice == "6":
                self.sortStudentByGPA()
            elif choice == "7":
                print("Exit")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manage = StudentManagement()
    manage.menu()
 
