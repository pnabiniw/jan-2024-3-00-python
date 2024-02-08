"""
Take two numbers input and divide a number by another number.
Handle the possible exceptions.

"""

try:
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter another number "))
    result = num1 / num2
except ValueError:
    print("Enter a valid number ")
except ZeroDivisionError:
    print("Please dont enter 0")
else:
    print(result)

