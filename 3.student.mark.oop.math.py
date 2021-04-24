import math
import curses


def getInput(stdscr):
    output = ''
    y, x = stdscr.getyx()
    done = False
    while not done:
        stdscr.clrtoeol()
        stdscr.addstr(y, x, output)
        char = stdscr.get_wch()
        if isinstance(char, str) and char.isprintable():
            output += char
        elif char in ('KEY_BACKSPACE', '\b', '\x7f'):
            output = output[:-1]
        elif char == '\n':
            done = True
        else:
            raise AssertionError(char)
    return output


class System:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def setStudents(self, stdscr):
        self.__students = []
        for i in range(self.__getInputNum__("students", stdscr)):
            stdscr.addstr("\nStudent " + str(i + 1) + ":")
            self.__students.append(Student(stdscr))

    def setCourses(self, stdscr):
        self.__courses = []
        for i in range(self.__getInputNum__("courses", stdscr)):
            stdscr.addstr("\nCourse " + str(i + 1) + ":")
            self.__courses.append(Course(stdscr))

    def getStudents(self):
        return self.__students

    def getCourses(self):
        return self.__courses

    @staticmethod
    def __getInputNum__(type_, stdscr):
        stdscr.clear()
        while True:
            try:
                stdscr.addstr("Enter the number of " + type_ + ": ")
                i = int(getInput(stdscr))
                return i
            except ValueError:
                stdscr.addstr("\nInvalid input. Try again\n")
                pass

    def __getInputCourse__(self, stdscr):
        while True:
            stdscr.addstr("\nEnter course name: ")
            courseName = getInput(stdscr)
            for course in self.__courses:
                if courseName == course.getName():
                    return course
            stdscr.addstr("\nInvalid course. Try again")

    @staticmethod
    def __swapStds__(std1, std2):
        swapStd = std1
        std1 = std2
        std2 = swapStd
        return std1, std2

    def __sortByGpa__(self, stdscr):
        sortedStudents = []
        for i in range(len(self.__students)):
            for j in range(i + 1, len(self.__students)):
                if self.__students[i].getGpa() < self.__students[j].getGpa():
                    self.__students[i], self.__students[j] = self.__swapStds__(self.__students[i], self.__students[j])
            sortedStudents.append(self.__students[i])
        for student in sortedStudents:
            stdscr.addstr("\nName: " + student.getName() + " - GPA: " + str(student.getGpa()))

    @staticmethod
    def __getActionId__(stdscr):
        stdscr.clear()
        stdscr.addstr("Actions: " +
                      "\n (1) List Courses" +
                      "\n (2) List Students" +
                      "\n (3) Set Marks (given course)" +
                      "\n (4) Get Marks (given course)" +
                      "\n (5) List Students (Sorted Gpa)" +
                      "\n (6) Finish")
        while True:
            try:
                stdscr.addstr("\nEnter a number for Action: ")
                i = int(getInput(stdscr))
                if i in (1, 2, 3, 4, 5, 6):
                    return i
            except ValueError:
                pass
            stdscr.addstr("\nInvalid input. Try again")

    def __action__(self, stdscr):
        while True:
            actionId = self.__getActionId__(stdscr)
            if actionId == 1:
                for course in self.__courses:
                    course.getInfo(stdscr)
                stdscr.addstr("\nPress any key to continue\n")
                stdscr.getch()
            elif actionId == 2:
                for student in self.__students:
                    student.getInfo(stdscr)
                stdscr.addstr("\nPress any key to continue\n")
                stdscr.getch()
            elif actionId == 3:
                course = self.__getInputCourse__(stdscr)
                course.setMarks(self.__students, stdscr)
                for student in self.__students:
                    for i in range(len(course.getMarks())):
                        if student.getName() == course.getMarks()[i][0]:
                            student.setMark(course.getName(), course.getMarks()[i][1], course.getWeight())
            elif actionId == 4:
                course = self.__getInputCourse__(stdscr)
                course.getInfo(stdscr)
                stdscr.addstr("\nPress any key to continue\n")
                stdscr.getch()
            elif actionId == 5:
                self.__sortByGpa__(stdscr)
                stdscr.addstr("\nPress any key to continue\n")
                stdscr.getch()
            else:
                stdscr.addstr("\nFinish. Thank you !")
                stdscr.addstr("\nPress any key to EXIT\n")
                stdscr.getch()
                break

    def __setCoursesInStds__(self):
        courseName = []
        for course in self.__courses:
            courseName.append(course.getName())
        for student in self.__students:
            student.setCourses(courseName)

    def run(self, stdscr):
        self.setStudents(stdscr)
        self.setCourses(stdscr)
        self.__setCoursesInStds__()
        self.__action__(stdscr)


class Student:
    def __init__(self, stdscr):
        self.__id = self.setIdSelf(stdscr)
        self.__name = self.setNameSelf(stdscr)
        self.__dob = self.setDoBSelf(stdscr)
        self.__gpa = 0
        self.__courses = [
            [],  # names of courses
            [],  # marks
            []   # weights
        ]

    def setId(self, id_):
        self.__id = id_

    @staticmethod
    def setIdSelf(stdscr):
        stdscr.addstr("\nEnter Id of Student: ")
        i = getInput(stdscr)
        return i

    def setName(self, name):
        self.__name = name

    @staticmethod
    def setNameSelf(stdscr):
        stdscr.addstr("\nEnter Name of Student: ")
        i = getInput(stdscr)
        return i

    def setDoB(self, dob):
        self.__dob = dob

    @staticmethod
    def setDoBSelf(stdscr):
        stdscr.addstr("\nEnter DoB of Student: ")
        i = getInput(stdscr)
        return i

    def setCourses(self, coursesName):
        self.__courses[0] = coursesName
        for i in range(len(coursesName)):
            self.__courses[1].append(0)
            self.__courses[2].append(0)

    def setMark(self, course, mark, weight):
        for i in range(len(self.__courses[0])):
            if course == self.__courses[0][i]:
                self.__courses[1][i] = mark
                self.__courses[2][i] = weight

    def setMarks(self, courses):
        for course in courses:
            for mark in course.marks:
                if mark[0] == self.__name:
                    self.setMark(course.getName(), mark, course.getWeight())

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDoB(self):
        return self.__dob

    def getCourses(self):
        return self.__courses

    def getGpa(self):
        self.__gpa = 0
        sumWeight = 0
        for i in range(len(self.__courses[0])):
            self.__gpa += self.__courses[1][i] * self.__courses[2][i]
            sumWeight += self.__courses[2][i]

        if sumWeight != 0:
            self.__gpa = math.floor(float(self.__gpa / sumWeight) * 10) / 10
        return self.__gpa

    def getInfo(self, stdscr):
        stdscr.addstr("\nStudent: " + self.__name + ":" +
                      "\n * Id: " + self.__id +
                      "\n * Dob: " + self.__dob +
                      "\n * Gpa: " + str(self.getGpa()))


class Course:
    def __init__(self, stdscr):
        self.__name = self.setNameSelf(stdscr)
        self.__id = self.setIdSelf(stdscr)
        self.__weight = self.setWeightSelf(stdscr)
        self.__marks = []

    def setName(self, name):
        self.__name = name

    @staticmethod
    def setNameSelf(stdscr):
        stdscr.addstr("\nEnter Name of Course: ")
        i = getInput(stdscr)
        return i

    def setId(self, id_):
        self.__id = id_

    @staticmethod
    def setWeightSelf(stdscr):
        stdscr.addstr("\nEnter Weight of Course: ")
        i = int(getInput(stdscr))
        return i

    def setWeight(self):
        return self.__weight

    @staticmethod
    def setIdSelf(stdscr):
        stdscr.addstr("\nEnter Id of Course: ")
        i = getInput(stdscr)
        return i

    def setMarks(self, students, stdscr):
        self.__marks = []
        stdscr.addstr("\n========")
        for student in students:
            mark = math.floor(self.setMark(student, stdscr) * 10) / 10
            self.__marks.append([student.getName(), mark])

    @staticmethod
    def setMark(student, stdscr):
        stdscr.addstr("\nEnter mark of " + student.getName() + ": ")
        i = float(getInput(stdscr))
        return i

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id

    def getMarks(self):
        return self.__marks

    def getWeight(self):
        return self.__weight

    def getInfo(self, stdscr):
        stdscr.addstr("\nCourse: " + self.__name + ":" +
                      "\n * Id: " + self.__id +
                      "\n * Marks: ")
        for i in range(len(self.__marks)):
            stdscr.addstr("\n     +   " + self.__marks[i][0] + ": " + str(self.__marks[i][1]))


System = System()


def main(stdscr):
    System.run(stdscr)


curses.wrapper(main)

