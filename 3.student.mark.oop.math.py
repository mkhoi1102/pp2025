import math
import numpy as np
import curses

gpa = []
students = []
courses = []
marks = []

class Student:
    def __init__(self, sid, sname, sdob):
        self.sid = sid
        self.sname = sname
        self.sdob = sdob
        self.gpa_value = 0.0

    def print_info(self, n):
        print(f"Student #{n + 1} information:")
        print('Name: ', self.sname)
        print('Id: ', self.sid)
        print('DOB: ', self.sdob)

class Course:
    def __init__(self, cid, cname, credits=1):
        self.cid = cid
        self.cname = cname
        self.credits = credits

    def print_info(self, n):
        print(f"Course #{n + 1} information:")
        print('Name: ', self.cname)
        print('Id: ', self.cid)
        print('Credits: ', self.credits)

class Mark:
    def __init__(self, cid, sid, mark):
        self.cid = cid
        self.sid = sid
        self.mark = mark

def calculate_gpa(student_id):
    total_weighted = 0.0
    total_credits = 0.0

    for record in marks:
        if record.sid == student_id:
            for course in courses:
                if course.cid == record.cid:
                    total_weighted += record.mark * course.credits
                    total_credits += course.credits

    if total_credits > 0:
        return total_weighted / total_credits
    return 0.0

def get_st_info():
    while True:
        try:
            students_number = int(input('Enter the number of students in your class: '))
            if students_number > 0:
                break
            else:
                print('Invalid value, please re-enter a positive number')
        except ValueError:
            print('Please enter a number: ')

    for n in range(students_number):
        sid = input(f"Enter #{n + 1} student's ID: ")
        sname = input(f"Enter #{n + 1} student's name: ")
        sdob = input(f"Enter #{n + 1} student's DOB: ")

        student = Student(sid, sname, sdob)
        students.append(student)

def get_courses_info():
    while True:
        try:
            courses_number = int(input('Enter the number of courses in your class: '))
            if courses_number > 0:
                break
            else:
                print('Invalid value, please re-enter a positive number')
        except ValueError:
            print('Please enter a number: ')

    for n in range(courses_number):
        cid = input(f"Enter #{n + 1} course's ID: ")
        cname = input(f"Enter #{n + 1} course's name: ")

        while True:
            try:
                credits = int(input(f"Enter #{n + 1} course's credits: "))
                if credits > 0:
                    break
                else:
                    print('Invalid value, please re-enter a positive number')
            except ValueError:
                print('Please enter a number: ')

        course = Course(cid, cname, credits)
        courses.append(course)

def print_students():
    print("\n      All students' information:\n")
    for n in range(len(students)):
        student = students[n]
        student.print_info(n)

def print_courses():
    print("\n      All courses' information:\n")
    for n in range(len(courses)):
        course = courses[n]
        course.print_info(n)

def input_marks():
    user_input = input("\nEnter course's ID to input students' marks: ").strip()

    for n in range(len(courses)):
        course = courses[n]
        if user_input == course.cid:
            for i in range(len(students)):
                student = students[i]
                while True:
                    try:
                        mark = float(input(f"Enter mark for student #{i + 1} ({student.sid}) "))
                        if 0 <= mark <= 10:
                            mark = math.floor(mark * 10) / 10
                            break
                        else:
                            print('Invalid value, please re-enter the value from 1 to 10')
                    except ValueError:
                        print('Please enter a number: ')
                mark = Mark(user_input, student.sid, mark)
                marks.append(mark)
            return
    print('Course ID not found!')

def print_marks():
    course_id = input("\nEnter course's ID to track students' mark: ").strip()
    print(f"\nMarks for course {course_id}:\n")
    flag = False

    for record in marks:
        if record.cid == course_id:
            flag = True
            print(f"Student {record.sid}: {record.mark}")
    if not flag:
        print('No marks for this course')

def print_gpa():
    print("\n      Students' GPA (sorted by GPA descending):\n")

    for student in students:
        student.gpa_value = calculate_gpa(student.sid)

    sorted_students = np.array(students)
    sorted_indices = np.argsort([-s.gpa_value for s in students])

    for idx in sorted_indices:
        student = students[idx]
        print(f"Student {student.sname} ({student.sid}): GPA {student.gpa_value:.2f}")

def decorate_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(5, 10, "---------- STUDENT MANAGEMENT MENU ----------", curses.COLOR_CYAN)
    stdscr.addstr(7, 10, "1. Input students' info", curses.COLOR_GREEN)
    stdscr.addstr(8, 10, "2. Input courses' info", curses.COLOR_GREEN)
    stdscr.addstr(9, 10, "3. Show students' info", curses.COLOR_YELLOW)
    stdscr.addstr(10, 10, "4. Show courses' info", curses.COLOR_YELLOW)
    stdscr.addstr(11, 10, "5. Input marks for students", curses.COLOR_YELLOW)
    stdscr.addstr(12, 10, "6. Show marks", curses.COLOR_YELLOW)
    stdscr.addstr(13, 10, "7. Show students' GPA", curses.COLOR_MAGENTA)
    stdscr.addstr(14, 10, "0. Exit", curses.COLOR_RED)
    stdscr.addstr(16, 10, "Enter a number: ", curses.COLOR_WHITE)
    stdscr.refresh()

def menu():
    print("\n----------Menu----------\n 1.Input students' info \n 2.Input courses' info \n 3.Show students' info \n 4.Show courses' info  \n 5.Input marks for students\n 6.Show marks\n 7.Show students' GPA\n 0.Exit ")

def main():
    while True:
        menu()
        try:
            user_input = int(input("\nEnter a number: "))
        except ValueError:
            print('Please enter a number')
            continue

        if user_input == 0:
            return
        if user_input == 1:
            get_st_info()
        if user_input == 2:
            get_courses_info()
        if user_input == 3:
            print_students()
        if user_input == 4:
            print_courses()
        if user_input == 5:
            input_marks()
        if user_input == 6:
            print_marks()
        if user_input == 7:
            print_gpa()

if __name__ == "__main__":
    main()
