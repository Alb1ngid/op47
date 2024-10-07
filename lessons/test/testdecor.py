import time
# декоратор
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print(f'функция {func.__name__} '
              f'выполнила код за: {exec_time}')
        return result
    return wrapper

@time_decorator
def square(n):
    return n * n
# print(f'квадрат числа 7:{square(7)}')

