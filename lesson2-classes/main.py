from Student import Student
from School import School

Sch = School()
Sch.get_students()
for i in range(5):
    Sch.add_student(Student(str(i), i))
for j in range(1, 5):
    for s in Sch.get_student_list():
        i = Sch.get_student_list().index(s) + 1
        s.add_grade(i**j)
Sch.get_students()
print("sorting !")
Sch.sort_by_avg(True)
Sch.get_students()
