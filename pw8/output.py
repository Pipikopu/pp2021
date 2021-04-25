from input import *


def getActionId(stdscr):
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



