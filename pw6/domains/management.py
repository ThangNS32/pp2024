import gzip
import pickle
from domains.student import Student
from domains.course import Course
import os
import numpy as np


class StudentManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__TinChis = {}

    def addStudent(self, get_string_input):
        num_students = int(get_string_input("Enter the number of students to add: "))
        for _ in range(num_students):
            student = Student("", "", "")
            student.input(get_string_input)
            self.__students.append(student)
        print(f"{num_students} students have been added.")

    def addCourse(self, get_string_input, get_int_input):
        num_courses = int(get_int_input("Enter the number of courses to add: "))
        for _ in range(num_courses):
            course = Course("", "", 0)
            course.input(get_string_input, get_int_input)
            self.__courses.append(course)
            self.__TinChis[course._CourseID] = course._TinChi
        print(f"{num_courses} courses have been added.")

    def inputMark(self, get_float_input):
        if not self.__students:
            print("No students available. Please add students first.")
            return
        if not self.__courses:
            print("No courses available. Please add courses first.")
            return

        course_id = input("Input Course ID for which you want to enter marks: ")
        if course_id not in self.__TinChis:
            print("Cannot find the course.")
            return

        for student in self.__students:
            mark = get_float_input(f"Enter mark for Student: {student._Name}, ID: {student._PersonID}: ")
            student.inputMark(course_id, mark)

    def calculateAllGPA(self):
        for student in self.__students:
            student.calculateGPA(self.__TinChis)

    def listStudent(self):
        if not self.__students:
            print("No students available!")
        else:
            print("\nList of Students:")
            for student in self.__students:
                print(student.list())

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

    def saveData(self):  # save data by pickle and gzip
        #Create a dict to save 
        data = {
            "students": self.__students,
            "courses": self.__courses,
            "credits": self.__TinChis
        }
        with gzip.open("data.pkl.gz", "wb") as f: #wb : write binary
            pickle.dump(data, f) #write to file
        print("Data has been saved successfully.")

    def loadData(self):  # Load by pickle and gzip
        if os.path.exists("data.pkl.gz"):
            with gzip.open("data.pkl.gz", "rb") as f: 
                data = pickle.load(f)
                self.__students = data.get("students", [])
                self.__courses = data.get("courses", [])
                self.__TinChis = data.get("credits", {})
            print("Data has been loaded successfully.")
        else:
            print("No saved data found.")
