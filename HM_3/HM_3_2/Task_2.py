from time import sleep


def my_decorator(func, call_count, start_sleep_time, factor, border_sleep_time):
    def wrapper(*args, **kwargs):
        print(f'Кол-во запусков = {call_count}')
        print('Начало работы')
        t = start_sleep_time
        func_result = func(*args, **kwargs)
        sleep(t)
        print(f'Запуск номер 1. Ожидание: {t} секунд. Результат декорируемой функций = {func_result}.')
        for i in range(2, call_count + 1):
            if t < border_sleep_time:
                t *= factor
            if t >= border_sleep_time:
                t = border_sleep_time
            sleep(t)
            print(f'Запуск номер {i}. Ожидание: {t} секунд. Результат декорируемой функций = {func_result}.')

        return func_result

    return wrapper


def multiplier(number: int):
    return number * 2


multiplier = my_decorator(multiplier, 3, 1, 2, 10)

multiplier(2)
