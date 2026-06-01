import os
import pickle
import zipfile
import tarfile
from domains.student import Student
from domains.course import Course
from domains.mark import Mark

students = []
courses = []
marks = []

STUDENTS_FILE = 'students.pkl'
COURSES_FILE = 'courses.pkl'
MARKS_FILE = 'marks.pkl'
ARCHIVE_FILE = 'students.dat'


def save_students():
    with open(STUDENTS_FILE, 'wb') as handle:
        pickle.dump(students, handle)


def save_courses():
    with open(COURSES_FILE, 'wb') as handle:
        pickle.dump(courses, handle)


def save_marks():
    with open(MARKS_FILE, 'wb') as handle:
        pickle.dump(marks, handle)


def get_st_info():
    while True:
        try:
            students_number = int(input('Enter the number of students in your class: '))
            if students_number > 0:
                break
            print('Invalid value, please re-enter a positive number')
        except ValueError:
            print('Please enter a number: ')

    for n in range(students_number):
        sid = input(f"Enter #{n + 1} student's ID: ")
        sname = input(f"Enter #{n + 1} student's name: ")
        sdob = input(f"Enter #{n + 1} student's DOB: ")

        student = Student(sid, sname, sdob)
        students.append(student)

    save_students()
    print(f"Saved {len(students)} student(s) to {STUDENTS_FILE}")


def get_courses_info():
    while True:
        try:
            courses_number = int(input('Enter the number of courses in your class: '))
            if courses_number > 0:
                break
            print('Invalid value, please re-enter a positive number')
        except ValueError:
            print('Please enter a number: ')

    for n in range(courses_number):
        cid = input(f"Enter #{n + 1} course's ID: ")
        cname = input(f"Enter #{n + 1} course's name: ")

        course = Course(cid, cname)
        courses.append(course)

    save_courses()
    print(f"Saved {len(courses)} course(s) to {COURSES_FILE}")


def input_marks():
    course_id = input("\nEnter course's ID to input students' marks: ").strip()
    for course in courses:
        if course_id == course.cid:
            for i, student in enumerate(students):
                while True:
                    try:
                        mark_value = float(input(f"Enter mark for student #{i + 1} ({student.sid}) "))
                        if 0 <= mark_value <= 10:
                            break
                        print('Invalid value, please re-enter the value from 0 to 10')
                    except ValueError:
                        print('Please enter a number: ')
                mark = Mark(course_id, student.sid, mark_value)
                marks.append(mark)

            save_marks()
            print(f"Saved {len(marks)} mark record(s) to {MARKS_FILE}")
            return

    print('Course ID not found!')


def _load_file(fileobj):
    return pickle.load(fileobj)


def load_data():
    if not os.path.exists(ARCHIVE_FILE):
        return

    print(f"Found {ARCHIVE_FILE}. Loading stored data...")
    try:
        try:
            with zipfile.ZipFile(ARCHIVE_FILE, 'r') as archive:
                with archive.open(STUDENTS_FILE) as sf:
                    students.extend(_load_file(sf))
                with archive.open(COURSES_FILE) as cf:
                    courses.extend(_load_file(cf))
                with archive.open(MARKS_FILE) as mf:
                    marks.extend(_load_file(mf))
        except zipfile.BadZipFile:
            with tarfile.open(ARCHIVE_FILE, 'r:*') as archive:
                with archive.extractfile(STUDENTS_FILE) as sf:
                    students.extend(_load_file(sf))
                with archive.extractfile(COURSES_FILE) as cf:
                    courses.extend(_load_file(cf))
                with archive.extractfile(MARKS_FILE) as mf:
                    marks.extend(_load_file(mf))

        print(f"Loaded {len(students)} student(s), {len(courses)} course(s), {len(marks)} mark record(s) from {ARCHIVE_FILE}.")
    except Exception as err:
        print(f'Could not load archive: {err}')


def select_compression_method():
    while True:
        choice = input('Select compression method (1 = zip, 2 = gzip): ').strip()
        if choice == '1':
            return 'zip'
        if choice == '2':
            return 'gzip'
        print('Please choose 1 or 2.')


def compress_files(method):
    if method == 'zip':
        with zipfile.ZipFile(ARCHIVE_FILE, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for path in [STUDENTS_FILE, COURSES_FILE, MARKS_FILE]:
                if os.path.exists(path):
                    archive.write(path, arcname=os.path.basename(path))
        print(f'Created {ARCHIVE_FILE} using zip compression.')
    else:
        with tarfile.open(ARCHIVE_FILE, 'w:gz') as archive:
            for path in [STUDENTS_FILE, COURSES_FILE, MARKS_FILE]:
                if os.path.exists(path):
                    archive.add(path, arcname=os.path.basename(path))
        print(f'Created {ARCHIVE_FILE} using gzip compression.')


def compress_before_exit():
    if not any(os.path.exists(path) for path in [STUDENTS_FILE, COURSES_FILE, MARKS_FILE]):
        print('No data files found to compress. Exiting without creating an archive.')
        return

    method = select_compression_method()
    compress_files(method)
