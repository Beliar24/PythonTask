def deprecated(replace):
    def decorator(funcs):
        def wrapper(*args, **kwargs):
            print(f"{funcs} deprecated. Call {replace} instead")
            return replace(*args, **kwargs)

        return wrapper

    return decorator


def new_func(a, b):
    return a * b


@deprecated(new_func)
def func(a, b):
    return a + b


print(func(5, 5))
