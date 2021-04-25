from domains.student import Student
from domains.course import Course


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


def getInputNum(type_, stdscr):
    stdscr.clear()
    while True:
        try:
            stdscr.addstr("Enter the number of " + type_ + ": ")
            i = int(getInput(stdscr))
            return i
        except ValueError:
            stdscr.addstr("\nInvalid input. Try again\n")
            pass


def setStudents(stdscr):
    students = []
    f = open("students.txt", "a")
    for i in range(getInputNum("students", stdscr)):
        stdscr.addstr("\nStudent " + str(i + 1) + ":")
        student = Student(stdscr)
        students.append(student)
        f.write(student.toString() + '\n')
    f.close()
    return students


def setCourses(stdscr):
    courses = []
    f = open("courses.txt", "a")
    for i in range(getInputNum("courses", stdscr)):
        stdscr.addstr("\nCourse " + str(i + 1) + ":")
        course = Course(stdscr)
        courses.append(course)
        f.write(course.toString() + '\n')
    f.close()
    return courses


def getInputCourse(courses, stdscr):
    while True:
        stdscr.addstr("\nEnter course name: ")
        courseName = getInput(stdscr)
        for course in courses:
            if courseName == course.getName():
                return course
        stdscr.addstr("\nInvalid course. Try again")


def setCoursesInStds(courses, students):
    courseName = []
    for course in courses:
        courseName.append(course.getName())
    for student in students:
        student.setCourses(courseName)