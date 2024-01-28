# Conditions are used to make decisions in Python (or in any programming language)
# There are few variations of if conditions in python

# 1. Simple if
# 2. if...else
# 3. if...elif...else
# 4. ternary if


# 1. Simple if
# if conditions don't necessarily take True or False. It can also take truthy or falsy values
a = 5
if a == 5:  # Here the statement after 'if' is 'True'
    print("The number is five")

if a:  # Here the statement after 'if' is truthy
    print("The number is non-zero")


# 2. if...else
a = 5
if a == 5:  # Here the statement after 'if' is 'True'
    print("The number is five")
else:
    print("The number is not five")

if a:  # Here the statement after 'if' is truthy
    print("The number is non-zero")
else:
    print("The number is zero")


# if...elif...else
a = 5
if a == 2:
    print("The number is 2")
elif a == 3:
    print("The number is 3")
elif a == 4:
    print("The number is 4")
else:
    print("The number is neither of 2, 3 or 4")


a = 2
if a == 2:
    print("The number is 2")
if a == 3:
    print("The number is 3")
if a == 4:
    print("The number is 4")
else:
    print("The number is not 4")


if a == 2:
    print("The number is 2")
elif a == 3:
    print("The number is 3")


# ternary if
a = 5
if a == 5:
    print("The number is 5")
else:
    print("The number is not 5")


print("The number is 5") if a == 5 else print("The number is not 5")  # ternary if


# Nested if

a = 10
b = 4
c = 5

if a == 5:
    if b == 2:
        print("a is 5 and b is 2")
    else:
        print("a is 5 but b is not 2")
else:
    print("The number is not 5")
