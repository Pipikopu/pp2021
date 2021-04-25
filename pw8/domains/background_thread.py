import threading
import pickle


class BackgroundThread(threading.Thread):
    def __init__(self, sleepTime, students, courses, stdscr):
        threading.Thread.__init__(self)
        self.__sleepTime = sleepTime
        self.__students = students
        self.__courses = courses
        self.__stdscr = stdscr

    def setVariable(self, students, courses):
        f = open('students.pickle', 'wb')
        pickle.dump(students, f)
        pickle.dump(courses, f)
        f.close()
        self.__stdscr.addstr(0, 40, "Done")
        self.__stdscr.refresh()
