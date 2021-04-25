import curses
from output import *
from os import path
import pickle
from domains.background_thread import BackgroundThread


def decompress(stdscr):
    if path.exists("students.pickle"):
        f = open("students.pickle", "rb")
        students = pickle.load(f)
        for student in students:
            student.getInfo(stdscr)
        stdscr.getch()
        stdscr.clear()
        courses = pickle.load(f)
        for course in courses:
            course.getInfo(stdscr)
        stdscr.getch()
        f.close()


def swapStds(std1, std2):
    swapStd = std1
    std1 = std2
    std2 = swapStd
    return std1, std2


def sortByGpa(students, stdscr):
    sortedStudents = []
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if students[i].getGpa() < students[j].getGpa():
                students[i], students[j] = swapStds(students[i], students[j])
        sortedStudents.append(students[i])
    for student in sortedStudents:
        stdscr.addstr("\nName: " + student.getName() + " - GPA: " + str(student.getGpa()))


class Action:
    def __init__(self, students, courses):
        self.__students = students
        self.__courses = courses
        self.__running = True

    def getStudents(self):
        return self.__students

    def getCourses(self):
        return self.__courses

    def running(self):
        return self.__running

    def run(self, stdscr):
        while self.__running:
            actionId = getActionId(stdscr)
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
                course = getInputCourse(self.__courses, stdscr)
                course.setMarks(self.__students, stdscr)
                for student in self.__students:
                    for i in range(len(course.getMarks())):
                        if student.getName() == course.getMarks()[i][0]:
                            student.setMark(course.getName(), course.getMarks()[i][1], course.getWeight())
            elif actionId == 4:
                course = getInputCourse(self.__courses, stdscr)
                course.getInfo(stdscr)
                stdscr.addstr("\nPress any key to continue\n")
                stdscr.getch()
            elif actionId == 5:
                sortByGpa(self.__students, stdscr)
                stdscr.addstr("\nPress any key to continue\n")
                stdscr.getch()
            else:
                stdscr.addstr("\nFinish. Thank you !")
                stdscr.addstr("\nPress any key to EXIT\n")
                stdscr.getch()
                self.__running = False


def main(stdscr):
    decompress(stdscr)
    students = setStudents(stdscr)
    courses = setCourses(stdscr)
    setCoursesInStds(courses, students)
    action = Action(students, courses)
    action.run(stdscr)
    thread = BackgroundThread(10, action.getStudents(), action.getCourses(), stdscr)
    thread.start()
    while True:
        thread.setVariable(action.getStudents(), action.getCourses())
        if not action.running():
            thread.join()
            break


curses.wrapper(main)