# Tuple packing and unpacking in Python

a = 1
print(type(a))  # int

a = 1,
print(type(a))  # tuple  (1,)

a = (1, 2)  # tuple

a = 1, 2  # This is tuple packing
print(a)  # (1, 2)

a, b = 1, 2
print(a)  # 1  int
print(b)  # 2  int

a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3

# a, b, c = 1, 2  # ValueError: not enough values to unpack
# a, b = 1, 2, 3  # ValueError: too many values to unpack


x = 10
y = 20

temp = x
x = y
y = temp

print(x)  # 20
print(y)  # 10


# Swapping data in python is quite easy
x, y = y, x  # (10, 20)

print(x)  # 10
print(y)  # 20
