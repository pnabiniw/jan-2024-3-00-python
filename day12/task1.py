# WAP to create a function which takes a number as an input and checks whether the number is odd or even

def is_even(num):
    return num % 2 == 0
    # if num % 2 == 0:
    #     return True
    # return False


num = int(input("Enter a number "))
result = is_even(num)
print(result)
result = is_even(4)
print(result)
