def some_message(func):
    def inner_func(*args, **kwargs):
        print("I am learning Decorator")
        return func(*args, **kwargs)
    return inner_func


@some_message
def addition(a, b):
    return a + b


print(addition(2, 3))


@some_message
def summ(a, b, c=12):
    return a + b + c


print(summ(2, 3))  # 9
