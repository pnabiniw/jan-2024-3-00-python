student = {"id": 2, "name": "Jane", "age": 30, "address": "KTM"}

key = input("Enter info you want to access ")
try:
    value = student[key]
except KeyError:
    print("The info is not provided for the student")
else:
    print(f"The {key} of the student is {value}")
