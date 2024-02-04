# WAP to create a decorator function which calcuates the total time to execute the following function



@execution_time
def func():
    for i in range(1000000000):
        continue
    print("Loop complete !!")


func()


import time

start = time.time()   # 112
a = 1
b = 2
print(a + b)
end = time.time()  # 117
total_time = end - start
print(total_time)
