def student_exists(student_id):
    try:
        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                saved_id, saved_name = line.split(",", 1)
                if saved_id == student_id:
                    return True
    except FileNotFoundError:
        return False

    return False


def course_exists(course_id):
    try:
        with open("courses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                saved_id, saved_name = line.split(",", 1)
                if saved_id == course_id:
                    return True
    except FileNotFoundError:
        return False

    return False


def enrollment_exists(student_id, course_id):
    try:
        with open("enrollments.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                saved_student_id, saved_course_id = line.split(",", 1)
                if saved_student_id == student_id and saved_course_id == course_id:
                    return True
    except FileNotFoundError:
        return False

    return False


def get_student_name(student_id):
    try:
        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                saved_id, name = line.split(",", 1)
                if saved_id == student_id:
                    return name
    except FileNotFoundError:
        pass

    return None


def get_course_name(course_id):
    try:
        with open("courses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                saved_id, course_name = line.split(",", 1)
                if saved_id == course_id:
                    return course_name
    except FileNotFoundError:
        pass

    return None


def get_student_id_by_name(student_name):
    try:
        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                student_id, name = line.split(",", 1)
                if name.lower() == student_name.lower():
                    return student_id
    except FileNotFoundError:
        pass

    return None


def get_course_id_by_name(course_name_input):
    try:
        with open("courses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                course_id, course_name = line.split(",", 1)
                if course_name.lower() == course_name_input.lower():
                    return course_id
    except FileNotFoundError:
        pass

    return None


def add_student():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()

    if student_id == "" or name == "":
        print("Student ID and name cannot be empty.")
        return

    if not student_id.isdigit():
        print("Student ID must be numbers only.")
        return

    if student_exists(student_id):
        print("This student ID already exists.")
        return

    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name}\n")

    print("Student added successfully!")


def add_course():
    course_id = input("Enter course ID: ").strip()
    course_name = input("Enter course name: ").strip()

    if course_id == "" or course_name == "":
        print("Course ID and course name cannot be empty.")
        return

    if not course_id.isdigit():
        print("Course ID must be numbers only.")
        return

    if course_exists(course_id):
        print("This course ID already exists.")
        return

    with open("courses.txt", "a") as file:
        file.write(f"{course_id},{course_name}\n")

    print("Course added successfully!")


def show_students():
    try:
        with open("students.txt", "r") as file:
            print("\nAvailable Students:")
            found = False

            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                student_id, name = line.split(",", 1)
                print(f"{name} (ID: {student_id})")
                found = True

            if not found:
                print("No students found.")
    except FileNotFoundError:
        print("No students found.")


def show_courses():
    try:
        with open("courses.txt", "r") as file:
            print("\nAvailable Courses:")
            found = False

            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                course_id, course_name = line.split(",", 1)
                print(f"{course_name} (ID: {course_id})")
                found = True

            if not found:
                print("No courses found.")
    except FileNotFoundError:
        print("No courses found.")


def enroll_student():
    show_students()
    show_courses()

    student_name = input("\nEnter student name: ").strip()
    course_name = input("Enter course name: ").strip()

    if student_name == "" or course_name == "":
        print("Student name and course name cannot be empty.")
        return

    student_id = get_student_id_by_name(student_name)
    course_id = get_course_id_by_name(course_name)

    if student_id is None:
        print("Student name does not exist.")
        return

    if course_id is None:
        print("Course name does not exist.")
        return

    if enrollment_exists(student_id, course_id):
        print("This student is already enrolled in this course.")
        return

    with open("enrollments.txt", "a") as file:
        file.write(f"{student_id},{course_id}\n")

    print("\nStudent enrolled successfully!")
    print(f"Student: {student_name} (ID: {student_id})")
    print(f"Course : {course_name} (ID: {course_id})")


def add_grade():
    show_students()
    show_courses()

    student_name = input("\nEnter student name: ").strip()
    course_name = input("Enter course name: ").strip()
    grade = input("Enter grade: ").strip()

    if student_name == "" or course_name == "" or grade == "":
        print("Student name, course name, and grade cannot be empty.")
        return

    student_id = get_student_id_by_name(student_name)
    course_id = get_course_id_by_name(course_name)

    if student_id is None:
        print("Student name does not exist.")
        return

    if course_id is None:
        print("Course name does not exist.")
        return

    if not enrollment_exists(student_id, course_id):
        print("This student is not enrolled in this course.")
        return

    try:
        grade_value = float(grade)
    except ValueError:
        print("Grade must be a number.")
        return

    if grade_value < 0 or grade_value > 100:
        print("Grade must be between 0 and 100.")
        return

    with open("grades.txt", "a") as file:
        file.write(f"{student_id},{course_id},{grade_value}\n")

    print("\nGrade added successfully!")
    print(f"Student: {student_name} (ID: {student_id})")
    print(f"Course : {course_name} (ID: {course_id})")
    print(f"Grade  : {grade_value}")


def view_student_report():
    show_students()
    student_name = input("\nEnter student name to view report: ").strip()

    if student_name == "":
        print("Student name cannot be empty.")
        return

    student_id = get_student_id_by_name(student_name)

    if student_id is None:
        print("Student name does not exist.")
        return

    print(f"\n=== Report for {student_name} (ID: {student_id}) ===")

    grades_found = False
    total = 0
    count = 0

    try:
        with open("grades.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue

                parts = line.split(",")
                if len(parts) != 3:
                    continue

                saved_student_id, course_id, grade = parts

                if saved_student_id == student_id:
                    course_name = get_course_name(course_id)
                    print(f"{course_name} (ID: {course_id}) : {grade}")
                    total += float(grade)
                    count += 1
                    grades_found = True

        if not grades_found:
            print("No grades found for this student.")
            return

        average = total / count
        print(f"Average: {average:.2f}")

    except FileNotFoundError:
        print("No grades file found.")


def main():
    while True:
        print("\n=== Student Course & Grade Tracker ===")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student")
        print("4. Add Grade")
        print("5. View Student Report")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            enroll_student()
        elif choice == "4":
            add_grade()
        elif choice == "5":
            view_student_report()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


main()