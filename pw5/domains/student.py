import math
from domains.person import Person

class Student(Person):
    def __init__(self,StudentID,StudentName,DoB):
        super().__init__(StudentID,StudentName,DoB)
        self.__marks = {}
        self.__gpa = 0

    def inputMark(self,CourseID,mark):
        round_DownMark = math.floor(mark * 10) / 10 #to round-down student scores to 1-digit decimal
        self.__marks[CourseID] = round_DownMark #Add Round Down Mark to dict Mark

    def listMark(self):
        return super().__str__() + ", Mark: {}".format(self.__marks) 
    
    def calculateGPA(self, TinChi):
        tongDiem = sum(
            self.__marks[course] * TinChi[course]
            for course in self.__marks
            if course in TinChi
        )
        tongTinChi = sum(TinChi[course] for course in self.__marks if course in TinChi)
        if tongTinChi > 0:
            self.__gpa = tongDiem / tongTinChi
        else:
            self.__gpa = 0
        return self.__gpa

    
    def getGPA(self):
        return self.__gpa
    
    def getMark(self):
        return self.__marks
