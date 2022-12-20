class Student:
    def __init__(self, name, student_id, grades=None):
        if grades is None:
            grades = []
        self.name = name
        self.id = student_id
        self.grades = grades

    def print_data(self, with_grade=True):
        print(f"Student: {self.name}\tid:{self.id}\tAvg: {self.get_avg()}")
        if with_grade:
            str_grades = "[ "
            for i in range(len(self.grades) - 1):
                str_grades += (str(self.grades[i]) + " | ")
            str_grades += str(self.grades[len(self.grades) - 1]) + " ]"
            print(str_grades + "\n")

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_avg(self):
        return sum(self.grades) / len(self.grades)

    def __add__(self, other):
        if len(self.name) > len(other.name):
            new_name = self.name
        else:
            new_name = other.name
        new_id = self.id + other.id
        if self.get_avg() > other.get_avg():
            return Student(new_name, new_id, self.grades)
        return Student(new_name, new_id, other.grades())

    def __str__(self):
        return f"Student: {self.name}\tid:{self.id}\ngrades:{self.grades}"

    def __gt__(self, other):
        return max(self.grades) > max(other.grades)


