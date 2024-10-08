import time

# Декоратор для измерения времени выполнения
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция '{func.__name__}' выполнена за {execution_time:.4f} секунд")
        return result
    return wrapper

# Функция для вычисления факториала
@time_decorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Функция для вычисления суммы чисел от 1 до n
@time_decorator
def sum_of_numbers(n):
    return sum(range(1, n + 1))

# Функция для нахождения n-го числа Фибоначчи
@time_decorator
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Функция для вычисления квадрата числа
@time_decorator
def square(n):
    return n * n

# Вызовы функций
print(f"Факториал 5: {factorial(5)}")
print(f"Сумма чисел от 1 до 10: {sum_of_numbers(10)}")
print(f"10-е число Фибоначчи: {fibonacci(2)}")
print(f"Квадрат числа 7: {square(7)}")
