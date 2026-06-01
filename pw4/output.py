import numpy as np

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
            print(f"Student {record.sid}: {record.mark}")
    if not flag:
        print('No marks for this course')

def calculate_gpa(student_id, courses, marks):
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

def print_gpa(students, courses, marks):
    print("\n      Students' GPA (sorted by GPA descending):\n")

    for student in students:
        student.gpa_value = calculate_gpa(student.sid, courses, marks)

    sorted_indices = np.argsort([-s.gpa_value for s in students])

    for idx in sorted_indices:
        student = students[idx]
        print(f"Student {student.sname} ({student.sid}): GPA {student.gpa_value:.2f}")
