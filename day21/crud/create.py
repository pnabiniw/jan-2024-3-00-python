import json
import os

FILENAME = "students.json"


def create_student():
    id = input("Enter id of the student ")
    name = input("Enter student name ")
    age = input("Enter student age")
    address = input("Enter student address")

    student = dict(id=id, name=name, age=age, address=address)

    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as fp:
            fp.write(json.dumps([student], indent=2))
    else:
        with open(FILENAME, "r+") as fp:
            students = json.loads(fp.read())  # '[{}, {}, {}]'  [{}, {}]
            students.append(student)
            fp.seek(0)
            fp.write(json.dumps(students, indent=2))
    print("Student added successfully !!")
    want_to_continue = input("Do you want to continue? (y/n)")
    return True if want_to_continue.lower() == 'y' else False
