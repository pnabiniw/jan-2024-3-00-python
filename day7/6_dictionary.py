# Dictionary is also an iterable in python
# It has the elements in the form of key-value pair and enclosed within curly braces
# Dictionary is also a mutable data type (like list and set)

# Creating dictionary
a = {}  # empty dictionary
b = dict()  # empty dictionary

student = {"name": "Jon", "age": 30, "email": "jon@email.com", "addresses": ["KTM", "PKR"]}
print(student)
student = dict(name="Jon", age=30, email="jon@email.com", addresses=["KTM", 'PKR'])
print(student)

# Dictionary values can be of any datatype
# But, dictionary keys must be immutable

data = {1: "Jon", 2: 30, 3: ["KTM", "PKR"]}  # valid dictionary
# data = {[1, 2]: "Jon", 2: 30, 3: ["KTM", "PKR"]}  # invalid dictionary


# Accessing dictionary data
student = {"name": "Jon", "age": 30, "email": "jon@email.com", "addresses": ["KTM", "PKR"]}
name = student["name"]  # Jon
age = student["age"]  # 30
email = student["email"]  # jon@email.com
# roll = student["roll"]  # KeyError

name = student.get("name")
age = student.get("age")
roll = student.get("roll")   # None
