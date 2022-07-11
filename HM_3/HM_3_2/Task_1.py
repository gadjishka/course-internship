def my_decorator(func):
    values = {}

    def wrapper(*args, **kwargs):
        if args[0] in values.keys():
            print('Res = ', values[args[0]])
            return values[args[0]]
        result = func(*args, **kwargs)
        values.update({args[0]: result})
        print("Res = ", result)
        return result

    return wrapper


@my_decorator
def multiplier(number: int):
    return number * 2
