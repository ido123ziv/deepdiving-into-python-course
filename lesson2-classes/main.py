from Student import Student
from School import School

Sch = School()
Sch.get_students()
for i in range(5):
    Sch.add_student(Student(str(i), i))
for s in Sch.get_student_list():
    i = Sch.get_student_list().index(s)
    s.add_grade(i**i + i)
Sch.get_students()
