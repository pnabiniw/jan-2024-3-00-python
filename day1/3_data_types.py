# Python has a set of built-in datatypes.
# Numbers
# List
# String
# Tuple
# Dictionary
# Set
# Boolean

# Mutable and Immutable Datatypes

# Mutable => All those objects which can be altered after their creation are the mutable objects
# E.g. List, Dictionary, Set are mutable
# Immutable =>All those objects which cant be altered after their creation are the immutable objects
# E.g. Numbers, Boolean, Tuple and String are immutable


# Numbers
# Numbers can either be integer, float or complex

a = 12
print(type(a))  # int


a = 12.2
print(type(a))  # float

b = 2e2  # 2 * 10**2
print(b)  # 200.0
print(type(b))  # float

b = 2e-2  # 2 * 10** -2
print(b)  # 0.02
print(type(b))  # float

# If operation is carried with any of the float type then the result is always float
print(2 + 2.0)  # 4.0


a = 1 + 2j
print(a)  # 1+2j
print(type(a))  # complex


# Methods, built in function and operations
