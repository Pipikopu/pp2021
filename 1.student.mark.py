def getInputNum(type_):
    while True:
        try:
            i = int(input("Enter the number of " + type_ + ": "))
            return i
        except ValueError:
            print("Invalid input. Try again")
            pass


def createCourse(index):
    course = {
        "name": input("Enter Course " + str(index + 1) + " name: "),
        "id": input("Enter Course id: "),
        "marks": []
    }
    return course


def createCourses():
    courses = []
    for i in range(getInputNum("courses")):
        courses.append(createCourse(i))
    return courses


def createStudent(index):
    student = {
        "id": input("Enter id of Student " + str(index + 1) + " : "),
        "name": input("Enter the name of Student: "),
        "dob": input("Enter DoB: ")
    }
    return student


def createStudents():
    stdList = []
    for index in range(getInputNum("students")):
        stdList.append(createStudent(index))
    return stdList


def getCourse(courses):
    while True:
        courseName = input("Enter course name: ")
        for i in range(len(courses)):
            if courseName == courses[i]["name"]:
                course = courses[i]
                return course
        print("Invalid course. Try again")


def getMark(student):
    while True:
        try:
            mark = int(input("Enter mark of " + student["name"] + ": "))
            return mark
        except ValueError:
            print("Invalid input. Try again")
            pass


def setMarks(course, students):
    print("=========")
    course["marks"] = []
    for i in range(len(students)):
        mark = getMark(students[i])
        course["marks"].append([students[i]["name"], mark])


def listCourses(courses):
    print("=========")
    print("List of Courses:")
    for i in range(len(courses)):
        print(" + " + courses[i]["name"])


def listStudents(students):
    print("=========")
    print("List of Students: ")
    for i in range(len(students)):
        print(" + Name: " + students[i]["name"])
        print("   Id: " + students[i]["id"])
        print("   Dob: " + students[i]["dob"])


def listMarks(course):
    print("=========")
    print("Marks of " + course["name"] + ": ")
    marks = course["marks"]
    for i in range(len(marks)):
        print(" + " + marks[i][0] + ": " + str(marks[i][1]))


def getActionId():
    print("=========")
    print("Actions: ")
    print(" (1) List Courses")
    print(" (2) List Students")
    print(" (3) Set Marks (given course)")
    print(" (4) Get Marks (given course)")
    print(" (5) Finish")
    while True:
        try:
            i = int(input("Enter a number for Action: "))
            if i in (1, 2, 3, 4, 5):
                return i
        except ValueError:
            pass
        print("Invalid input. Try again")


def action(students, courses):
    while True:
        actionId = getActionId()
        if actionId == 1:
            listCourses(courses)
        elif actionId == 2:
            listStudents(students)
        elif actionId == 3:
            setMarks(getCourse(courses), students)
        elif actionId == 4:
            listMarks(getCourse(courses))
        else:
            print("Finish. Thank you !")
            break


def run():
    students = createStudents()
    courses = createCourses()

    action(students, courses)


run()
