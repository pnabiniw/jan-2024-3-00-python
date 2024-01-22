# Identifiers
# Any user defined names in the program are called identifiers
# Examples: module name, function name, class name, variable name

# Rules of naming an identifier
# 1. Identifiers are case-sensitive. Uppercase and lowercase matter.
A = 5
a = 3
print(a)
print(A)
abc = 2
Abc = 5

# 2. Identifiers can't be a keyword
# There are 35 keywords in python and they cant be used as an identifier
# def = 5  # invalid because def is a keyword
# help("keywords") displays all the python keywords


# 3. Identifiers can't contain special symbols like @, #, $ etc.
# a@ = 3  # Invalid


# 4. Identifiers can contain digits but it should not start with a digit
a1 = 12  # Valid
# 1a = 4  # Invalid


# 5. Identifiers can contain underscore (_) and can also start with an underscore
a_ = 12
a_b = 12
_a = 12
_ = 12
__ = 1


# Syntax in Python
# Indentation is a big issue in python to represent a block of code

a = 5
if a == 5:
    print("the number is 5")
print(a)


a = 1; b = 2

message = "Hello World. " \
          "I am learning Python"


a = 1
print(a)  # 1
