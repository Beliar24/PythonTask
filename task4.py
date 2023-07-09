
def counter(func):
    def wrapper():
        wrapper.counter += 1
        return func()

    wrapper.counter = 0
    return wrapper


@counter
def some_func():
    print("Fail")


some_func()
some_func()
some_func()

print(some_func.counter)