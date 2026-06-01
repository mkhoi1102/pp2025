import math

def print_students(students):
    print("\n      All students' information:\n")
    for n in range(len(students)):
        student = students[n]
        student.print_info(n)

def print_courses(courses):
    print("\n      All courses' information:\n")
    for n in range(len(courses)):
        course = courses[n]
        course.print_info(n)

def print_marks(marks):
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
