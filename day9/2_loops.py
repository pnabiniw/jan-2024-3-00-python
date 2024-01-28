# Loops are used to perform certain tasks repeatedly in a program
# They are also called as iteration

# There are two types of loop in python
# 1. for loop
# 2. while loop

# We do not have do...while loop in python


# for loops
# for loops are applied in iterables in python (not in condition)

# for loop syntax in C language
# for(i=0;i<=10;i++){
#     statement
# }

for num in ["a", "e", "i", "o", "u"]:
    print(num)  # "a", "e", "i", "o", "u"


# range()
# range is a built-in function in python which gives the range of numbers

print(list(range(10)))  # gives 0 to 9
print(list(range(2, 10)))  # gives 2 to 9
print(list(range(2, 10, 2)))  # gives 2, 4, 6, 8


# WAP to print even numbers in the range of 0 to 50
print(list(range(0, 51, 2)))


for i in range(0, 51):
    if i % 2 == 0:
        print(i)
