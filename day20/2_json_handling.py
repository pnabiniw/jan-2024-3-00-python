# JSON stands for JavaScript Object Notation
# It is a file format to store data so that it could be rendered and parsed easily
# It looks similar to the python dictionary
# They are mostly used to share information among different entities (Frontend and Backend,
# Mobile and Backend, backend and backend)
# Python has a built-in json module

import json
filename = "student.json"

student = {'name': 'Alex', 'age': 20, "address": "KTM"}

with open(filename, "w") as fp:
    data = json.dumps(student)
    fp.write(data)


with open(filename, "r") as fp:
    student = fp.read()
    student = json.loads(student)

print(student)
print(student["age"])
print(type(student))



