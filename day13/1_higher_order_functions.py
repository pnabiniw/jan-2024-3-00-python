# If a function takes another function as an argument then the function is called
# higher-order function

# Some important features of python functions
# 1. Functions can be stored in a variable
def multiply(a, b):
    return a * b


m = multiply
result = m(2, 3)
print(result)  # 6


# 2. Function can be an element of python data structures like list and tuple
def addition(a, b):
    return a + b


def multiply(a, b):
    return a * b


data = [addition, multiply, 1, 2, "a"]
x = data[0](2, 3)
print(x(2, 3))  # 5


# 3. A function can take another function as an argument

# Built-in higher order functions in python
# map(), filter() and reduce()
