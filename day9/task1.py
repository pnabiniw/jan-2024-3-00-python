# WAP to take a number input. If the number is divisible by 3 print "fizz", if divisible by
# 5 print "buzz", if divisible by both 3 and 5 print "fizzbuzz". If not divisible by both 3 and 5
# then print the number as it is.

num = int(input("Enter a number "))  # 15
if num % 5 == 0 and num % 3 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print(num)

