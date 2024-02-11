# Given a list of students ["Jon", "Jane", "Hary", "Alex"] create a list of dictionaries with
# random address and random exam marks. Dump the list to a JSON file students.json. Again read the json file
# and print the address of "Hary"

import json
student_names = ["Jon", "Jane", "Hary", "Alex"]
students = [dict(name=name, address="KTM", marks=100) for name in student_names]  # [{}, {}, {}, {}]  # list comp.

filename = "students.json"
with open(filename, "w") as fp:
    fp.write(json.dumps(students, indent=2))

with open(filename, "r") as fp:
    students = json.loads(fp.read())

print(students)
for student in students:
    if student["name"] == "Hary":
        print(f"Address of Hary is {student['address']}")
        break
