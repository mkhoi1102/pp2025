import input as inp
import output as out

def menu():
    print("\n----------Menu----------\n 1.Input students' info \n 2.Input courses' info \n 3.Show students' info \n 4.Show courses' info  \n 5.Input marks for students\n 6.Show marks\n 0.Exit ")

def main():
    inp.load_data()
    while True:
        menu()
        try:
            user_input = int(input("\nEnter a number: "))
        except ValueError:
            print('Please enter a number')
            continue

        if user_input == 0:
            inp.compress_before_exit()
            return
        if user_input == 1:
            inp.get_st_info()
        if user_input == 2:
            inp.get_courses_info()
        if user_input == 3:
            out.print_students(inp.students)
        if user_input == 4:
            out.print_courses(inp.courses)
        if user_input == 5:
            inp.input_marks()
        if user_input == 6:
            out.print_marks(inp.marks)

if __name__ == '__main__':
    main()
