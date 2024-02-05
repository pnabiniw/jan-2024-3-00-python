# OOP approach (Object-Oriented Programming) is a programming paradigm in which problems are broken
# down into classes and objects
# Classes are the blueprints of how an object looks
# Objects are the actual instance of a class

# "class" keyword is used to create a class in Python
# The naming convention of every class should follow CamelCase in Python


class Vehicle:  # python class
    engine_type = "petrol"   # Class Attribute => property

    # init is a constructor function which is called when an object of this class is created
    def __init__(self, color, number_of_seats):  # constructor
        self.color = color  # instance attribute => instance property
        self.number_of_seats = number_of_seats  # instance attribute => instance property

    def get_info(self):  # instance method
        return f"The vehicle engine type is {self.engine_type}. Its color is {self.color} and it has " \
               f"{self.number_of_seats} seats"

    def set_color(self, new_color):
        self.color = new_color


# This is how we create object in python  Classname()
v1 = Vehicle("red", 6)  # vehicle object
v2 = Vehicle("green", 4)  # vehicle object

# We use dot operator with object to access attributes of a class
print(v1.engine_type)  # petrol
print(v2.engine_type)  # petrol

print(v1.color)  # red
print(v2.color)  # green

print(v1.get_info())
v1.set_color("yellow")
print(v1.color)  # yellow

v1.color = "orange"
print(v1.color)  # orange


# Attributes Category
# => Class Attribute
#   => Class Property
#   => Class Method
# => Instance Attribute
#    => Instance Property
#    => Instance Method
