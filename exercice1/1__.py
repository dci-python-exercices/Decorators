def annoying_decorator(func):
    def wrapper():
        greeting = func()
        if greeting == "Hi":
            greeting = "Don't use Hi! with me, please!"
        else:
            greeting = "hello, Sir"
        return greeting

    return wrapper


@annoying_decorator
def greetings():
    return "Hi"


if __name__ == '__main__':
    print(greetings())
