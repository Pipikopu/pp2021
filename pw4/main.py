import curses
from output import *


def main(stdscr):
    students = setStudents(stdscr)
    courses = setCourses(stdscr)
    setCoursesInStds(courses, students)
    action(students, courses, stdscr)


curses.wrapper(main)