# While loop is used with truthy / falsy statements or conditions and logics which gives truthy / falsy

a = 1
while a < 10:
    print(a)
    a += 1

# It is important to update the condition variable from inside the while loop otherwise the loop goes infinite

# But sometimes there is the need of infinite loop
# while True:  # infinite loop
#     a = 1
#     print(a)


# We can also use else statement with while loop
a = 1
while a < 10:
    print(a)
    a += 1
else:
    print("The loop is executed completely")
