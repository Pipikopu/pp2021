import sys
sys.path.append('..')
# noinspection PyUnresolvedReferences
import input
import math


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
        i = input.getInput(stdscr)
        return i

    def setName(self, name):
        self.__name = name

    @staticmethod
    def setNameSelf(stdscr):
        stdscr.addstr("\nEnter Name of Student: ")
        i = input.getInput(stdscr)
        return i

    def setDoB(self, dob):
        self.__dob = dob

    @staticmethod
    def setDoBSelf(stdscr):
        stdscr.addstr("\nEnter DoB of Student: ")
        i = input.getInput(stdscr)
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