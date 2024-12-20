import numpy as np
from domains.student import Student
from domains.course import Course 

class StudentManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__TinChis = {}

    def addStudent(self,get_string_input):
        num_students = int(get_string_input("Enter the number of student to add: "))
        for i in range (num_students):
            student = Student("","","")
            student.input(get_string_input)
            self.__students.append(student)
        print(f"{num_students} student have been added.")

    def addCourse(self,get_string_input,get_int_input):
        num_course = get_int_input("Enter the number of Course to add: ")
        for i in range(num_course):
            course = Course("","","")
            course.input(get_string_input,get_int_input)
            self.__courses.append(course)
            self.__TinChis[course._CourseID] = course._TinChi
        print(f"{num_course} course have been added")

    def inputMark(self,get_float_input):
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
            mark = get_float_input("Enter mark for Student: {}, ID: {}: ".format(student._Name,student._PersonID))
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

