class Course:
    def __init__(self,CourseID,CourseName ,TinChi):
        self._CourseID = CourseID
        self._CourseName = CourseName
        self._TinChi = TinChi

    def __str__(self):
        return "CourseID: {}, CourseName: {}".format(self._CourseID,self._CourseName)
    
    def input(self,get_string_input, get_int_input):
        self._CourseID = get_string_input("Enter Course ID: ")
        self._CourseName = get_string_input("Enter Course Name: ")
        self._TinChi = get_int_input("Enter Credits for the Course: ")

    def list(self):
        return str(self)