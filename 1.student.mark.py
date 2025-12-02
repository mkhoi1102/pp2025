students = []
courses = []
marks = []

def get_students_in4() :
    while True :
        try :
            students_number = int(input('Enter a number of students in your class: '))
            if students_number > 0 :
                break
            else :
                print("Invalid value, please re-enter the positive value")
        except ValueError :
            print('Please enter a number: ')

    for n in range(students_number) :
        print(f'Student #{n + 1}')
        sid = input("Enter the student's ID: ").strip()
        sname = input("Enter the student's name: ").strip()
        sdob = input("Enter the student's DOB: ").strip()
        students.append({'id': sid, 'name': sname, 'dob': sdob})
    return students

get_students_in4()

def print_students() :
    print("\nAll students' information:\n")

    for n in range(len(students)) :
        student = students[n]
        print(f"Student #{n+1} info:\n")
        print(f" ID: {student['id']}")
        print(f" Name: {student['name']}")
        print(f" DoB: {student['dob']}\n")

print_students()

def get_courses_in4() :
    while True :
        try :
            courses_number = int(input('Enter a number of courses in your class: '))
            if courses_number > 0 :
                break
            else :
                print("Invalid value, please re-enter the positive value")
        except ValueError :
            print('Please enter a number: ')

    for n in range(courses_number) :
        print(f'Course #{n + 1}')
        cid = input("Enter the course's ID: ").strip()
        cname = input("Enter the course's name: ").strip()
        courses.append({'id': cid, 'name': cname})
    return courses

get_courses_in4()

def print_courses() :
    print("\nAll courses' information:\n")

    for n in range(len(courses)) :
        course = courses[n]
        print(f"Course #{n+1} info:\n")
        print(f" ID: {course['id']}")
        print(f" Name: {course['name']}\n")

print_courses()

def input_marks() :
    user_input = input("Enter course's ID to input students' mark: ").strip()

    for n in range(len(courses)) :
        course = courses[n]
        if user_input == course['id'] :
            for i in range(len(students)) :
                student = students[i]
                while True :
                    try :
                        mark = float(input(f"Enter mark for student #{i+1} ({student['id']}): "))
                        if 0 <= mark <= 10:
                            break
                        else :
                            print('Invalid value, please re-enter the value from 1 to 10')
                    except ValueError :
                        print("Please enter a number: ")

                marks.append({"course_id": user_input, "sid": student["id"], "mark": mark})
            return

    print("Course ID not found!")

input_marks()

def print_marks() :
    course_id = input("\nEnter course's ID: ").strip()
    print(f"\nMarks for course {course_id}:\n")
    flag = False

    for record in marks :
        if record["course_id"] == course_id:
            flag = True
            print(f"Student {record['sid']}: {record['mark']}")
    if not flag :
        print('No marks for this course')

print_marks()