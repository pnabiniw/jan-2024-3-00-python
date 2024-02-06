"""
Create a class Circle with an attribute radius. Create two objects of circle c1 and c2.
Add the radius of the circles and print the result.
Do the above task using a method and then a magic method.
Compare the size of the circle and print the result using magic method.

"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def add_radius(self, other):
        return self.radius + other.radius

    def __add__(self, other):
        return self.radius + other.radius

    def __mul__(self, other):
        return self.radius * other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius


c1 = Circle(5)
c2 = Circle(10)
result = c1.radius + c2.radius
print("Sum of radii is", result)

result = c1.add_radius(c2)

result = c1.__add__(c2)  # here __add__ is a magic method
result = c1 + c2

print(c1 > c2)
print(c1 < c2)
