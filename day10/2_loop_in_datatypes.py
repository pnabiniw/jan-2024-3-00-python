# Loops can be used in the datatypes which are iterables
# Iterable datatypes are list, string, tuple, set, dictionary


# Looping in a list
vowels = ["a", "e", "i", "o", "u"]
for each in vowels:
    print(each)  # a e i o u

# Looping in a tuple
vowels = ("a", "e", "i", "o", "u")
for each in vowels:
    print(each)  # a e i o u


# Looping in a string
data = "Hello World. I am learning python"
for each in data:
    print(each)  # H e l l o  W o r l d .  I a m  l e a r n i n g  p y t h o n


# Looping in a dictionary
student = {"name": "Raju", "email": "r@email.com", "address": "KTM"}

for each in student:
    print(each)  # name  email  address


print(student.values())  # dict_values(["Raju", "r@email.com", "KTM"])
for each in student.values():
    print(each)  # Raju  r@email.com  KTM


for each in student.keys():
    print(each)  # name  email  address


print(student.items())  # dict_items([("name", "Raju), ("email", "r@email.com"), ("address", "KTM")])
for each in student.items():
    print(each)  # ("name", "Raju")   ("email", "r@email.com")   ("address", "KTM")

for key, value in student.items():
    print(key)  # "name"  "email"  "address"
    print(value)  # "Raju"  "r@email.com"  "KTM"


# We can use "else" with loop in Python
data = ["a", "e", "i", "o", "u"]
for each in data:
    print(each)  # a  e  i  o  u
else:
    print("This block runs if the iteration is done completely")
