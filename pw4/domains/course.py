import sys
sys.path.append('..')
# noinspection PyUnresolvedReferences
import input
import math


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
        i = input.getInput(stdscr)
        return i

    def setId(self, id_):
        self.__id = id_

    @staticmethod
    def setWeightSelf(stdscr):
        stdscr.addstr("\nEnter Weight of Course: ")
        i = int(input.getInput(stdscr))
        return i

    def setWeight(self):
        return self.__weight

    @staticmethod
    def setIdSelf(stdscr):
        stdscr.addstr("\nEnter Id of Course: ")
        i = input.getInput(stdscr)
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
        i = float(input.getInput(stdscr))
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