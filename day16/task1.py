"""
Create a class Person with instance attributes name and age. Create a method get_details in this class
to print name and age.
Create another class Employee with attributes salary and designation and inherits
the Person class. Create a method get_details in this class to print name, age, salary and designation of
the Employee.

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name is {self.name} and age is {self.age}"


class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):  # Overridden Method
        print(super().get_details())
        return f"Salary is {self.salary} and designation is {self.designation}"


e1 = Employee("Jane", 24, 34000, "Manager")
print(e1.get_details())


# we can use super() function to call the method of parent class from the child class given that both the
# methods are same

# This is also the concept of method overriding

