def login_required(func):
    def inner_func(*args, **kwargs):
        pw = input("Enter password ")
        if pw == "1234":
            return func(*args, **kwargs)
        else:
            return "Incorrect Password"
    return inner_func


@login_required
def addition(a, b):
    return a + b


print(addition(2, 3))
