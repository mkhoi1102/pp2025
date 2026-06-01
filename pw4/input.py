import math
from domains import Student, Course, Mark

def get_st_info(students):
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

def get_courses_info(courses):
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

def input_marks(students, courses, marks):
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
