class Student:
    def __init__(self):
        self.id = input("Enter id of Student: ")
        self.name = input("Enter name of Student: ")
        self.dob = input("Enter DoB of Student: ")

    def setId(self, id_):
        self.id = id_

    def setName(self, name):
        self.name = name

    def setDoB(self, dob):
        self.dob = dob

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getDoB(self):
        return self.dob

    def toString(self):
        print("Student: " + self.name + ":")
        print(" * Id: " + self.id)
        print(" * Dob: " + self.dob)


class Course:
    def __init__(self):
        self.name = input("Enter Course name: ")
        self.id = input("Enter Course id: ")
        self.marks = []

    def setName(self, name):
        self.name = name

    def setId(self, id_):
        self.id = id_

    def setMarks(self, students):
        print("=========")
        for student in students:
            mark = int(input("Enter mark of " + student.getName() + ": "))
            self.marks.append([student.getName(), mark])

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getMarks(self):
        return self.marks

    def toString(self):
        print("Course: " + self.name + ":")
        print(" * Id: " + self.id)
        print(" * Marks: ")
        for i in range(len(self.marks)):
            print("     +   " + self.marks[i][0] + ": " + str(self.marks[i][1]))


def getInputNum(type_):
    while True:
        try:
            i = int(input("Enter the number of " + type_ + ": "))
            return i
        except ValueError:
            print("Invalid input. Try again")
            pass


def getInputCourse(courses):
    while True:
        courseName = input("Enter course name: ")
        for course in courses:
            if courseName == course.getName():
                return course
        print("Invalid course. Try again")


def getActionId():
    print("==========")
    print("Actions: ")
    print(" (1) List Courses")
    print(" (2) List Students")
    print(" (3) Set Marks (given course)")
    print(" (4) Get Marks (given course)")
    print(" (5) Finish")
    while True:
        try:
            i = int(input("Enter a number for Action: "))
            if i in (1, 2, 3, 4, 5):
                return i
        except ValueError:
            pass
        print("Invalid input. Try again")


def action(students, courses):
    while True:
        actionId = getActionId()
        if actionId == 1:
            for course in courses:
                print(course.getName())
        elif actionId == 2:
            for student in students:
                print(student.getName())
        elif actionId == 3:
            course = getInputCourse(courses)
            course.setMarks(students)
        elif actionId == 4:
            course = getInputCourse(courses)
            course.toString()
        else:
            print("Finish. Thank you !")
            break


def run():
    students = []
    courses = []
    for i in range(getInputNum("students")):
        print("Student " + str(i + 1) + ":")
        students.append(Student())
    for i in range(getInputNum("courses")):
        print("Course " + str(i + 1) + ":")
        courses.append(Course())

    action(students, courses)


run()