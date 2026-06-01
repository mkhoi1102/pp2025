import math

gpa = []
students = []
courses = []
marks = []

class Student:
    def __init__(self, sid, sname, sdob):
        self.sid = sid
        self.sname = sname
        self.sdob = sdob

    def print_info(self, n):
        print(f"Student #{n + 1} information:")
        print('Name: ', self.sname)
        print('Id: ', self.sid)
        print('DOB: ', self.sdob)

class Course:
    def __init__(self, cid, cname):
        self.cid = cid
        self.cname = cname
    
    def print_info(self, n):
        print(f"Course #{n + 1} information:")
        print('Name: ', self.cname)
        print('Id: ', self.cid)

class Mark:
    def __init__(self, cid, sid, mark):
        self.cid = cid
        self.sid = sid
        self.mark = mark

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

        course = Course(cid, cname)
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
            print(f"Student {record.sid}: {math.floor(record.mark)}")
    if not flag:
        print('No marks for this course')

def credits_sum():
    student_id = input("\nEnter student's ID to track credits: ").strip()
    flag = False

    for record in marks:
        if record.sid == student_id:
            flag == True
             


def menu():
    print("\n----------Menu----------\n 1.Input students' info \n 2.Input courses' info \n 3.Show students' info \n 4.Show courses' info  \n 5.Input marks for students\n 6.Show marks\n 0.Exit ")

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
          


main()