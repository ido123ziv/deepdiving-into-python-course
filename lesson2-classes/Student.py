class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id
        self.grades = []

    def print_data(self):
        print(f"Student: {self.name}\nid:{self.id}\ngrades:{self.grades}")

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_avg(self):
        return sum(self.grades) / len(self.grades)

