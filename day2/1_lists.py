# List are sequential datatypes (iterables) in python enclosed in big brackets => []
# They are the mutable datatypes

# Creating list in python
a = []  # empty list
b = list()  # empty list. list() is a built-in function to create a list

c = [1, 2, 3]  # Non-empty list
# List elements can be of different datatypes.

d = [1, 2.1, "hello", [1, 2], (4, 5), list()]

# Unlike in list, arrays elements must be homogenous


# Accessing list elements
# List elements can be accessed using indexing or slicing

# Indexing
vowels = ["a", "e", "i", "o", "u"]
print(vowels[0])  # a
print(vowels[4])  # u
print(vowels[-1])  # u
print(vowels[-4])  # e
# print(vowels[5])  # IndexError
# print(vowels[-6])  # IndexError


# Slicing
data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(data[0:7])  # ["a", "b", "c", "d", "e", "f", "g"]
print(data[7:])  # ["h", "i", "j"]
print(data[3:8])  # ["d", "e", "f", "g", "h"]
print(data[:5])  # ["a", "b", "c", "d", "e"]

print(data[:-8])  # ["a", "b"]
print(data[-4:])  # ["g", "h", "i", "j"]
print(data[-8:-2])  # ["c", "d", "e", "f", "g", "h"]
print(data[-3:-7])  # []
print(data[2:9:2])  # ["b", "d", "f", "h"]


print(data[3:9])  # ["d", "e", "f", "g", "h", "i"]
print(data[8:2])  # []
print(data[5:])  # ["f", "g", "h", "i", "j"]
print(data[:4])  # ["a", "b", "c", "d"]
print(data[-9:-3])  # ["b", "c", "d", "e", "f", "g"]
print(data[-8:8])  # ["c", "d", "e", "f", "g", "h"]
print(data[9:-7])  # []
print(data[-4:-9])  # []


# List Operations

# Concatenation (+)
a = [1, 2, 3]
b = [4, 5, 6]
result = a + b
print(result)  # [1, 2, 3, 4, 5, 6]


# Repetition/broadcast Operation (*)
a = [1, 2]
print(a * 3)  # [1, 2, 1, 2, 1, 2]


# Membership Operation ("in" and "not in")
print("a" in ["a", "e", "i"])  # True
print("e" not in ["a", "e", "i"])  # False

