# Operators are the special symbols which are used ro carry out arithmetical and logical operations.
# Like in any other language python also has it's set of operators

# Arithmetic Operators
# Logical Operators
# Relational Operators
# Assignment Operators
# Membership Operators
# Identity Operators


# Arithmetic Operators (+, -, /, *, **, %)
a = 1  # Python statement
b = 2  # Python statement

result = a + b
print("The result of the sum is", result)

result = b ** 2
print(result)   # 4

result = 5 % 2
print(result)   # 1

result = 5 / 2
print(result)  # 2.5


# Relational / Comparison Operators (>, <, >=, <=, ==, !=)
# The result of comparison operations are either True or False

a = 20
b = 15
print(a > b)  # True
print(a < b)  # False
print(a == b)  # False
print(a >= b)  # True
print(a <= b)  # False
print(a != b)  # True


# Logical Operators (and, or, not)
# The result of logical operations are either True or False

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

print(not True)  # False
print(not False)  # True


a = 1
b = 15
c = 15

if a > b or b == c:
    print("Hello World")


# Assignment Operator (=, +=, -=, *=, /=)
message = "Hello World"
b = 5
b = b + 5
print(b)  # 10

b += 5
print(b)  # 15

b -= 5
print(b)  # 10


# Membership Operators ('in' and 'not in')
# The result of membership operation is also True or False
# Membership operators are used in the sequential data (iterables) e.g. list, array, tuple etc.
vowels = ['a', 'e', 'i', 'o', 'u']
print("a" in vowels)  # True
print("A" in vowels)  # False
print("A" not in vowels)  # True
print("a" not in vowels)  # False


# Identity Operator ('is' and 'is not')
# The result of identity operations are also in True/False
# It checks whether the two objects are same or not

a = 4
b = 4
print(a is b)  # True, Same object

a = []
b = []
print(a is b)   # False, different object



