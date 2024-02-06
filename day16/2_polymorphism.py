# Poly refers to many and 'morphism' refers to forms. So, polymorphism is many forms of same function,
# methods or operators


a = 1
b = 2
print(a + b)  # Sum => 3

a = "1"
b = "2"
print(a + b)  # Concatenation => 12


# We mainly study two topics in polymorphism
# Method / Function Overloading
# Operator Overloading


# Method / Function Overloading

def addition(x, y):
    return x + y


def addition(p, q, r):
    return p + q + r


result = addition(2, 3)  # Error
# print(result)
result = addition(2, 3, 4)
print(result)  # 9

# Python doesnt support function and method overloading. If a function is defined multiple times in a same
# python file then only the last definition is considered


class Person:
    def __init__(self, name, age, address):
        self.name = name   # public attribute
        self.age = age   # protected attribute because it has single underscore at the beginning
        self.address = address  # private attribute because it has double underscore at the beginning

    def get_details(self):
        return f"Name is {self.name} and age is {self.age}"

    def get_details(self):
        return f"Name is {self.name} and age is {self.age} and address is {self.address}"


# Operator Overloading
# Every operator has their respective methods defined inside the built-in python classes. Such methods of
# operators are called the magic methods

x = 2
y = 3
r = x + y
print(r)

r = x.__add__(y)
print(r)
