# enumerate is also a built-in function in python
# It takes iterable as an input

data = ["a", "e", "i", "o", "u"]
result = enumerate(data)
print(list(result))  # [(0, 'a'), (1, 'e'), (2, 'i'), (3, 'o'), (4, 'u')]


# We can start the count from the number of our choice
result = enumerate(data, start=1)
print(list(result))  # [(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o'), (5, 'u')]


data = ["a", "e", "i", "o", "u"]
for i in enumerate(data):
    print(i)  # (0, a)  (1, e)  (2, i)   (3, o)  (4, u)


for index, value in enumerate(data):
    print(index, end="")  # 0 1 2 3 4
    print(value, end="")  # a e i o u
