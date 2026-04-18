from student import Student


# Global collection variable
students = []


def collect_student_data():
    print("Enter information for 3 students:")

    for number in range(1, 4):
        print(f"\nStudent {number}")

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        student_id = input("Enter student ID: ")

        # Local variable used to create one student object
        student = Student(name, age, student_id)
        students.append(student)


def print_student_names_and_ages():
    print("\nStudent names and ages in entered order:")
    for student in students:
        print(f"{student.name} - {student.age}")


def sort_students_by_age():
    return sorted(students, key=lambda student: student.age)


def print_sorted_students():
    sorted_students = sort_students_by_age()

    print("\nStudents sorted by age:")
    for student in sorted_students:
        print(f"{student.name} - {student.age}")


if __name__ == "__main__":
    collect_student_data()
    print_student_names_and_ages()
    print_sorted_students()
