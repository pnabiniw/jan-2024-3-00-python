class Person:
    def __init__(self, age):
        self.age = age

    @classmethod
    def from_birth_year(cls, year):
        age = 2024 - year
        return Person(age)


p1 = Person(30)
print(p1.age)  # 30


p2 = Person.from_birth_year(1994)
print(p2.age)  # 30
