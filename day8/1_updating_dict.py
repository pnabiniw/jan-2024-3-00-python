# Jan 26

student = {"name": "Hary", "age": 30, "address": "KTM"}

age = student.get("age")
print(age)  # 30
age = student["age"]
print(age)  # 30

# roll = student["roll"]  # KeyError
roll = student.get("roll")  # None


student["roll"] = 30
print(student)  # {"name": "Hary", "age": 30, "address": "KTM", "roll": 30}

student["name"] = "HARRY"
print(student)  # {"name": "HARRY", "age": 30, "address": "KTM", "roll": 30}


data = ["a", "e", "o", "u"]
data.insert(2, "i")
print(data)  # ["a", "e", "i" "o", "u"]

# data[4] = "U"
# print(data)  # ["a", "e", "i" "o", "U"]
