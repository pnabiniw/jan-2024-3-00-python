# difference()
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
result = s1.difference(s2)  # s1 - s2
print(result)  # {1, 2, 3}

result = s1 - s2
print(result)


result = s1.intersection(s2)
print(result)  # {4, 5}
result = s1 & s2
print(result)  # {4, 5}

result = s1.union(s2)
print(result)  # {1, 2, 3, 4, 5, 6, 7, 8}
result = s1 | s2
print(result)  # {1, 2, 3, 4, 5, 6, 7, 8}

result = s1.symmetric_difference(s2)
print(result)  # {1, 2, 3, 6, 7, 8}
result = s1 ^ s2
print(result)  # {1, 2, 3, 6, 7, 8}

s1.symmetric_difference_update(s2)
print(s1)  # {1, 2, 3, 6, 7, 8}


result = s1.isdisjoint(s2)
print(result)  # False



a = {1, 2, 3, 4, 5}
b = {2, 3}

print(b.issubset(a))  # True
print(a.issubset(b))  # False

print(a.issuperset(b))  # True
print(b.issuperset(a))  # False

