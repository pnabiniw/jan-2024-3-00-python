# Exceptions in python are handled using try...except block
# There are different variations of try...except block

# pep8 => document (guideline) which explains python coding standard


try:
    num = int(input("Enter a number"))
    print(num)
except:
    print("Enter a valid number")


try:
    num = int(input("Enter a number"))
    print(num)
except ValueError:
    print("Enter a valid number")


try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    print(num1 + num2)
except ValueError:
    print("Enter a valid number")
except TypeError:
    print("Use proper Operator")


try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    print(num1 + num2)
except (ValueError, TypeError):
    print("Enter a valid number")


# We can use else block with try...except
try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
except ValueError:
    print("Enter a valid number")
else:
    print(num1 + num2)


# Finally we can add 'finally' block in try...except
try:
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
except ValueError:
    print("Enter a valid number")
else:
    print(num1 + num2)
finally:
    print("This code is always executed")


fp = open("msg.txt", "r")

try:
    print(fp.read())
except:
    print("Some Error")
finally:
    fp.close()
