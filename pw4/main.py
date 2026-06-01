from input import get_st_info, get_courses_info, input_marks
from output import print_students, print_courses, print_marks, print_gpa

students = []
courses = []
marks = []

def menu():
    print("\n----------Menu----------")
    print(" 1. Input students' info")
    print(" 2. Input courses' info")
    print(" 3. Show students' info")
    print(" 4. Show courses' info")
    print(" 5. Input marks for students")
    print(" 6. Show marks")
    print(" 7. Show students' GPA")
    print(" 0. Exit")

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
            get_st_info(students)
        if user_input == 2:
            get_courses_info(courses)
        if user_input == 3:
            print_students(students)
        if user_input == 4:
            print_courses(courses)
        if user_input == 5:
            input_marks(students, courses, marks)
        if user_input == 6:
            print_marks(marks)
        if user_input == 7:
            print_gpa(students, courses, marks)

if __name__ == "__main__":
    main()
