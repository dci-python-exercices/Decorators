def verbose(func):
    def wrapper(*args):
        temp = func(*args)
        arguments = [arg for arg in args]
        return print(f"{func.__name__} invoked with {tuple(arguments).__str__()} -> {temp} ")

    return wrapper


@verbose
def sum_two(a, b):
    return a + b


if __name__ == "__main__":
    sum_two(1, 3)
