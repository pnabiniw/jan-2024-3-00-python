# There are four main pillars of OOP
# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. Abstraction

# Encapsulation is the process of hiding the class attributes so that it can only be accessed outside the class
# if required

# There are three different types of encapsulated attributes Private, Public and Protected

class Person:
    def __init__(self, name, age, address):
        self.name = name   # public attribute
        self._age = age   # protected attribute because it has single underscore at the beginning
        self.__address = address  # private attribute because it has double underscore at the beginning

    def get_details(self):
        return f"Name is {self.name} and age is {self._age} and address is {self.__address}"


p1 = Person("Jon", 21, "KTM")
print(p1.name)  # Jon  here name is a public attribute
print(p1._age)   # here _age is protected but it is still accessible from outside the class. Though this way
# of coding is not recommended

# print(p1.__address)  # This gives AttributeError
print(p1.get_details())
