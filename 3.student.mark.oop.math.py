import math


class System:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def setStudents(self):
        self.__students = []
        for i in range(self.__getInputNum__("students")):
            print("Student " + str(i + 1) + ":")
            self.__students.append(Student())

    def setCourses(self):
        self.__courses = []
        for i in range(self.__getInputNum__("courses")):
            print("Course " + str(i + 1) + ":")
            self.__courses.append(Course())

    def getStudents(self):
        return self.__students

    def getCourses(self):
        return self.__courses

    @staticmethod
    def __getInputNum__(type_):
        while True:
            try:
                i = int(input("Enter the number of " + type_ + ": "))
                return i
            except ValueError:
                print("Invalid input. Try again")
                pass

    def __getInputCourse__(self):
        while True:
            courseName = input("Enter course name: ")
            for course in self.__courses:
                if courseName == course.getName():
                    return course
            print("Invalid course. Try again")

    @staticmethod
    def __swapStds__(std1, std2):
        swapStd = std1
        std1 = std2
        std2 = swapStd
        return std1, std2

    def __sortByGpa__(self):
        sortedStudents = []
        for i in range(len(self.__students)):
            for j in range(i + 1, len(self.__students)):
                if self.__students[i].getGpa() < self.__students[j].getGpa():
                    self.__students[i], self.__students[j] = self.__swapStds__(self.__students[i], self.__students[j])
            sortedStudents.append(self.__students[i])
        for student in sortedStudents:
            print("Name: " + student.getName() + " - GPA: " + str(student.getGpa()))
        return sortedStudents

    @staticmethod
    def __getActionId__():
        print("==========")
        print("Actions: ")
        print(" (1) List Courses")
        print(" (2) List Students")
        print(" (3) Set Marks (given course)")
        print(" (4) Get Marks (given course)")
        print(" (5) List Students (Sorted Gpa)")
        print(" (6) Finish")
        while True:
            try:
                i = int(input("Enter a number for Action: "))
                if i in (1, 2, 3, 4, 5, 6):
                    return i
            except ValueError:
                pass
            print("Invalid input. Try again")

    def __action__(self):
        while True:
            actionId = self.__getActionId__()
            if actionId == 1:
                for course in self.__courses:
                    course.getInfo()
            elif actionId == 2:
                for student in self.__students:
                    student.getInfo()
            elif actionId == 3:
                course = self.__getInputCourse__()
                course.setMarks(self.__students)
                for student in self.__students:
                    for i in range(len(course.marks)):
                        if student.getName() == course.marks[i][0]:
                            student.setMark(course.getName(), course.marks[i][1], course.getWeight())
            elif actionId == 4:
                course = self.__getInputCourse__()
                course.getInfo()
            elif actionId == 5:
                self.__sortByGpa__()
            else:
                print("Finish. Thank you !")
                break

    def setCoursesInStds(self):
        courseName = []
        for course in self.__courses:
            courseName.append(course.getName())
        for student in self.__students:
            student.setCourses(courseName)

    def run(self):
        self.setStudents()
        self.setCourses()
        self.setCoursesInStds()
        self.__action__()


class Student:
    def __init__(self):
        self.id = input("Enter id of Student: ")
        self.name = input("Enter name of Student: ")
        self.dob = input("Enter DoB of Student: ")
        self.gpa = 0
        self.courses = [
            [],  # names of courses
            [],  # marks
            []   # weights
        ]

    def setId(self, id_):
        self.id = id_

    def setName(self, name):
        self.name = name

    def setDoB(self, dob):
        self.dob = dob

    def setCourses(self, coursesName):
        self.courses[0] = coursesName
        for i in range(len(coursesName)):
            self.courses[1].append(0)
            self.courses[2].append(0)

    def setMark(self, course, mark, weight):
        for i in range(len(self.courses[0])):
            if course == self.courses[0][i]:
                self.courses[1][i] = mark
                self.courses[2][i] = weight
                print(self.courses)

    def setMarks(self, courses):
        for course in courses:
            for mark in course.marks:
                if mark[0] == self.name:
                    self.setMark(course.getName(), mark, course.getWeight())

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getDoB(self):
        return self.dob

    def getCourses(self):
        return self.courses

    def getGpa(self):
        self.gpa = 0
        sumWeight = 0
        for i in range(len(self.courses[0])):
            self.gpa += self.courses[1][i] * self.courses[2][i]
            sumWeight += self.courses[2][i]

        if sumWeight != 0:
            self.gpa = math.floor(float(self.gpa / sumWeight) * 10) / 10
        return self.gpa

    def getInfo(self):
        print("Student: " + self.name + ":")
        print(" * Id: " + self.id)
        print(" * Dob: " + self.dob)
        print(" * Gpa: " + str(self.getGpa()))


class Course:
    def __init__(self):
        self.name = input("Enter Course name: ")
        self.id = input("Enter Course id: ")
        self.weight = int(input("Enter Course weight: "))
        self.marks = []

    def setName(self, name):
        self.name = name

    def setId(self, id_):
        self.id = id_

    def setMarks(self, students):
        self.marks = []
        print("=========")
        for student in students:
            mark = math.floor(float(input("Enter mark of " + student.getName() + ": ")) * 10) / 10
            self.marks.append([student.getName(), mark])

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getMarks(self):
        return self.marks

    def getWeight(self):
        return self.weight

    def getInfo(self):
        print("Course: " + self.name + ":")
        print(" * Id: " + self.id)
        print(" * Marks: ")
        for i in range(len(self.marks)):
            print("     +   " + self.marks[i][0] + ": " + str(self.marks[i][1]))
        print(self.marks)


System = System()
System.run()





