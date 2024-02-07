"""
Create a class Department with parameters name and number_of_students.
Create a method total students, which takes department object as a parameter and
return the total number of students from all departments.

"""


class Department:
    def __init__(self, name, number_of_students):
        self.name = name
        self.number_of_students = number_of_students

    def total_students(self, *others):  # (d2, d3)
        students_in_each = [other.number_of_students for other in others]   # [12, 15]
        return sum(students_in_each) + self.number_of_students


d1 = Department("CS", 20)
d2 = Department("IT", 12)
d3 = Department("Engg", 15)
d4 = Department("Elex", 40)

students_count = d1.total_students(d2, d3, d4)
# students_count = d2.total_students(d1, d3, d4)
print(students_count)  # 32
