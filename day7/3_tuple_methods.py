# Tuple has only two methods, count() and index() because tuple is immutable

# count()
a = (1, 2, 3, 1, 2, 1, 1, 3, 3)
result = a.count(3)
print(result)  # 3
print(a)  # (1, 2, 3, 1, 2, 1, 1, 3, 3)

a = [1, 2, 3]
result = a.append(4)
print(result)  # None
print(a.append(4))  # None
print(a)  # [1, 2, 3, 4]


# index()
data = ("a", "b", "c", "a", "c", "d")
result = data.index("c")
print(result)  # 2

result = data.index("c", 4, 6)
print(result)  # 4
