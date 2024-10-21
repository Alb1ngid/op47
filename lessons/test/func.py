# Функция для вычисления факториала
from  testdecor import time_decorator
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
# Вызовы функций
print(f"Факториал 5: {factorial(5)}")
print(f"Сумма чисел от 1 до 10: {sum_of_numbers(10)}")
print(f"2-е число Фибоначчи: {fibonacci(2)}")

