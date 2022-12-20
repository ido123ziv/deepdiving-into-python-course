class School:
    def __init__(self):
        self.students = []

    def get_student_list(self):
        return self.students

    def add_student(self, student):
        arr = list(filter(lambda x: x.id == student.id, self.students))
        if len(arr) == 0:
            self.students.append(student)
        else:
            print("Student Already exists")

    def get_students(self):
        print("Here are all the students:\n")
        for s in self.students:
            s.print_data()
            print("Student Avg is: {}".format(s.get_avg()))
