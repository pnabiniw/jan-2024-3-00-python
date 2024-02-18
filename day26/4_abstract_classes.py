# Those classes from which we can't make an object are the abstract classes.

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "It Barks !!"

d = Dog()
print(d.sound())
