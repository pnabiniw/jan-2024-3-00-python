# If a function is called from within the same function then it is called recursive function

a = 0


def func():
    global a
    print(a)
    a += 1
    if a < 11:
        func()  # recursive call

func()


# Calculate the factorial of 5 using:
# 1. Simple Loop
# 2. reduce() function
# 3. Recursive function


result = 1
for i in range(1, 6):
    result = result * i

print(result)  # 120


from functools import reduce
result = reduce(lambda x, y: x * y, range(1, 6))
print(result)


def factorial(num):
    if num == 0:
        return 1
    if num < 0:
        return "N/A"
    return num * factorial(num - 1)


result = factorial(5)
print(result)  # 120


# 5 * factorial(4) => 5 * 24 = 120
# 4 * factorial(3)  => 4 * 6 = 24
# 3 * factorial(2) => 3 * 2 = 6
# 2 * factorial(1) => 2 * 1 = 2
# 1 * factorial(0) => 1 * 1 = 1
