from Student import Student
from School import School

Sch = School()
# Sch.get_students()
for j in range(1, 5):
    Sch.add_student(Student(str(j), j, [x+j for x in range(1, 5)]))
    print(Sch.get_student_list()[j-1])
    # for i in range(10):
    #     Sch.get_student_list()[j-1].add_grade(j+i)
    #     # s.add_grade(i**j)
Sch.get_students()
"""
print("sorting !")
Sch.sort_by_avg(True)
Sch.get_students()
"""