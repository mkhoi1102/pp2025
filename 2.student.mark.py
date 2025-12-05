students = []
courses = []
marks = []

class Student:
    def __init__(self, sid, sname, sdob):
        self.sid = sid
        self.sname = sname
        self.sdob = sdob

    def print_info(self, n):
        print(f"Student #{n+1} info:\n")
        print("Student's ID: ", self.sid)
        print("Student's name: ", self.sname)
        print("Student's DOB: ", self.sdob)

class Course:
    def __init__(self, cid, cname):
        self.cid = cid
        self.cname = cname
    
    def print_course(self, n):
        print(f"Course #{n + 1} info: ")
        print("Course's name: ", self.cid)
        print("Course's ID: ", self.cname)

class Mark:
    def __init__(self, cid, sid, mark):
        self.cid = cid
        self.sid = sid
        self.mark = mark
    

def get_courses_info():
    while True:
        try:
            courses_number = int(input('Enter the number of courses: '))
            if courses_number > 0:
                break
            else:
                print("Invalid value, please re-enter the positive value")
        except ValueError:
            print("Please enter a positive number: ")

    for n in range(courses_number):
        cid = input(f"Enter #{n + 1} course's ID: ")
        cname = input(f"Enter #{n + 1} course's name: ")

        course = Course(cid, cname)
        courses.append(course)

get_courses_info()


def print_courses():
    print("\n    All courses information: \n")
    for n in range(len(courses)):
        course = courses[n]
        course.print_course(n)
    
print_courses()

def get_students_info():
    while True:
        try:
            students_number = int(input('Enter the number of students in your class: '))
            if students_number > 0:
                break
            else:
                print("Invalid value, please re-enter the positive value")
        except ValueError:
            print("Please enter a positive number: ")


    for n in range(students_number):
        sid = input(f"Enter #{n + 1} student's ID: ")
        sname = input(f"Enter #{n + 1} student's name: ")
        sdob = input(f"Enter #{n + 1} student's DOB: ")
    
        student = Student(sid, sname, sdob)
        students.append(student)


get_students_info()

def print_students():
    print("\n    All students information: \n")

    for n in range(len(students)):
        student = students[n]
        student.print_info(n)

print_students()

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

input_marks()

def print_marks():
    course_id = input(" Enter course's ID: ").strip()
    print(f"\nMarks for course {course_id}:\n")
    flag = False

    for record in marks:
        if record.cid == course_id:
            flag = True
            print(f"Student {record.sid}: {record.mark}")
    if not flag:
        print('No marks for this course')

print_marks()

                


    
        