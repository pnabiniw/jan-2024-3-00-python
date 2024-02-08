# Errors in Python (or in any language) can broadly be categorized as:
# 1. Syntactic Error
# 2. Non-Syntactic Error (Runtime Error and Logical Errors)

# Syntax is the grammar of programming language

# There are following categories of Non-syntactic error

# TypeError
# a = 1
# b = "Hello"
# print(a + b)  # It raises TypeError


# ValueError
num = int(input("Enter a number "))
# Here, if we provide input other than numbers then it raises ValueError


# IndexError
data = ["a", "e", "i", "o", "u"]
print(data[4])  # u
print(data[10])  # IndexError. List Index Out of Range
print(data[-6])  # IndexError

# KeyError
student = {"name": "Jon", "address": "PKR"}
print(student.get("roll"))  # None
print(student["roll"])  # KeyError


# ZeroDivisionError
print(2/0)  # ZeroDivisionError


# NameError
print(z)  # NameError because z is not defined above

