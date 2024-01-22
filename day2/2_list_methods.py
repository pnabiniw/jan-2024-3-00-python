# What are methods?
#=> Methods are the functions defined inside a class
# Methods must be called using an object


# append()
a = [1, 2, 3]
a.append(5)
print(a)  # [1, 2, 3, 5]


# extend()
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)  # [1, 2, 3, 4, 5, 6]


b = ["a", "e", "i"]
result = b.append("o")
print(result)  # None
print(b)  # ["a", "e", "i", "o"]

# insert()
b = ["a", "e", "o", "u"]
b.insert(2, "i")
print(b)  # ["a", "e", "i", "o", "u"]


# remove()
b = ["a", "e", "i", "o", "u"]
b.remove("u")
print(b)  # ["a", "e", "i", "o"]
# b.remove("z")  # ValueError. If remove() is used for the item not present in the list


# pop()
b = ["a", "e", "i", "o", "u"]
result = b.pop()
print(b)  # ["a", "e", "i", "o"]
print(result)  # u

result = b.pop(2)
print(result)  # i
print(b)  # ["a", "e", "o"]


# clear()
b = ["a", "e", "i", "o", "u"]
b.clear()
print(b)  # []

# index()
b = ["a", "e", "i", "o", "u", "a", "e", "i", "a", "e"]
result = b.index("o")
print(result)  # 3
result = b.index("a")
print(result)  # 0

result = b.index("a", 4, 9)
print(result)  # 5


# count()
b = ["a", "e", "i", "o", "u", "a", "e", "i", "a", "e"]
result = b.count("a")
print(result)  # 3


# sort()
data = [3, 5, 1, 6, 2, 7]
data.sort()
print(data)  # [1, 2, 3, 5, 6, 7]

data.sort(reverse=True)
print(data)  # [7, 6, 5, 3, 2, 1]


# reverse()
data = [3, 5, 1, 6, 2, 7]
data.reverse()
print(data)  # [7, 2, 6, 1, 5, 3]


# copy()
a = [1, 2, 3]
b = a
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]
print(a is b)  # True

b = a.copy()
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]
print(a is b)  # False


