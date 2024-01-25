# sum()
# It is a built-in function which takes iterable of numbers as an input

r = sum([1, 2, 3])  #
print(r)  # 6

r = sum((1, 2, 3))  #
print(r)  # 6

r = sum([1, 2, 3])
print(r)  # 6


# max()
# It also takes iterable as an input and returns the maximum from that iterable

print(max(4, 5, 1, 8, 10))  # 10


# min()
# It also takes iterable as an input and returns the minimum from that iterable
print(min(4, 5, 1, 8, 10))  # 1


# sorted()
# It also takes iterable and returns the sorted data

data = sorted([7, 1, 3, 2, 10, 15])
print(list(data))

data = sorted([7, 1, 3, 2, 10, 15], reverse=True)
print(list(data))  # [15, 10, 7, 3, 2, 1]


# reversed()
# It also takes iterable and returns the reversed data

data = reversed([7, 1, 3, 2, 10, 15])
print(list(data))  # [15, 10, 2, 3, 1, 7]
