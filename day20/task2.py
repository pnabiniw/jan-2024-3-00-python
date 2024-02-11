## Reading the binary file

import pickle
with open("output.dat", "rb") as fp:
    students = pickle.load(fp)

print(students)  # [{}, {}, {}]
print(students[1]['name'])
print(students[1]["marks"])

for student in students:
    if student["name"] == "Jane":
        print(f"The marks of Jane is {student['marks']}")
        break

