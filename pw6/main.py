import curses
import zipfile
from output import *
from os import path


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


def action(students, courses, stdscr):
    while True:
        actionId = getActionId(stdscr)
        if actionId == 1:
            for course in courses:
                course.getInfo(stdscr)
            stdscr.addstr("\nPress any key to continue\n")
            stdscr.getch()
        elif actionId == 2:
            for student in students:
                student.getInfo(stdscr)
            stdscr.addstr("\nPress any key to continue\n")
            stdscr.getch()
        elif actionId == 3:
            course = getInputCourse(courses, stdscr)
            course.setMarks(students, stdscr)
            for student in students:
                for i in range(len(course.getMarks())):
                    if student.getName() == course.getMarks()[i][0]:
                        student.setMark(course.getName(), course.getMarks()[i][1], course.getWeight())
        elif actionId == 4:
            course = getInputCourse(courses, stdscr)
            course.getInfo(stdscr)
            stdscr.addstr("\nPress any key to continue\n")
            stdscr.getch()
        elif actionId == 5:
            sortByGpa(students, stdscr)
            stdscr.addstr("\nPress any key to continue\n")
            stdscr.getch()
        else:
            stdscr.addstr("\nFinish. Thank you !")
            stdscr.addstr("\nPress any key to EXIT\n")
            stdscr.getch()
            break


def main(stdscr):
    decompress(stdscr)
    students = setStudents(stdscr)
    courses = setCourses(stdscr)
    setCoursesInStds(courses, students)
    action(students, courses, stdscr)
    f = open('students.pickle', 'wb')
    pickle.dump(students, f)
    pickle.dump(courses, f)
    f.close()


curses.wrapper(main)