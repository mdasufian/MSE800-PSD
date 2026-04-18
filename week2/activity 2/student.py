class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"
