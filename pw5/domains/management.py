import numpy as np
from domains.student import Student
from domains.course import Course 
import os
import zipfile
import pickle

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

    def saveData(self): #Lưu dữ liệu vào tập tin 
        with open("students.txt","w") as f:
            for student in self.__students:
                f.write("{} ,{} ,{} \n".format(student._PersonID, student._Name , student._DoB))

        with open("courses.txt","w") as f:
            for course in self.__courses:
                f.write("{} ,{} ,{} \n".format(course._CourseID,course._CourseName,course._TinChi))

        with open("marks.txt","w") as f:
            for student in self.__students:
                marks = ",".join(
                    f"{CourseID} : {mark}" for CourseID ,mark in student._Student__marks.items() #Chuyển đổi dict của sinh viên thành 1 chuỗi để dễ lưu trữ , Ngăn cách nhau bằng dấu ","
                )
                f.write("{} : {}\n".format(student._PersonID,marks))

    def loadData(self): #Add data into file
        if os.path.exists("students.txt"):
            with open("students.txt","r") as f:
                for line in f: #Duyệt từng dòng trong file
                    id , name, dob = line.strip().split(",") #strip : Loại bỏ các kí tự khoảng trắng dư thừa , split(",") : Tách dòng thành một list và dấu "," làm dấu phân tách
                    self.__students.append(Student(id,name,dob))

        if os.path.exists("courses.txt"):
            with open("courses.txt","r") as f:
                for line in f:
                    id , name , credits = line.strip().split(",")
                    self.__courses.append(Course(id,name,int(credits)))
                    self.__TinChis[id] = int(credits)

        if os.path.exists("marks.txt"):
            with open("marks.txt","r") as f:
                for line in f:
                    parts = line.strip().split(":", 1)  # Chỉ tách thành 2 phần dựa vào dấu ":" đầu tiên
                    if len(parts) == 2:
                        studentid, marks = parts
                    else:
                        print(f"Invalid format in line: {line}")

                    student = next((s for s in self.__students if s._PersonID == studentid), None)#Tìm sinh viên trong list có mã studentid tương ứng , trả về None nếu không tìm thấy sinh viên 
                    if student:
                        for pair in marks.split(","): #Duyệt qua từng cặp courseid:mark trong marks
                            if ":" in pair:
                                try:
                                    courseid, mark = pair.split(":")
                                    # Xử lý dữ liệu
                                except ValueError:
                                    print(f"Error while unpacking pair: {pair}")
                            else:
                                print(f"Invalid pair format: {pair}")
                            student.inputMark(courseid,float(mark))
                        
    def compressFile(self): #Nén dữ liệu thành tệp "students.dat"
        with zipfile.ZipFile("students.dat","w") as f:
            for fileName in ["students.txt","courses.txt","marks.txt"] :
                if os.path.exists(fileName):
                    f.write(fileName)

    def decompressFile(self): #Giải nén
        if os.path.exists("students.dat"):
            with zipfile.ZipFile("students.dat","r") as f:
                f.extractall()


