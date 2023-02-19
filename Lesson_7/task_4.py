from time import time
from functools import wraps
from typing import NoReturn


def measure_execution_time(func):
    """Decorator to measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Скорость выполнения: {end - start:.7f} sec.')
        return result
    return wrapper


@measure_execution_time
def func_range(n: int) -> NoReturn:
    """This function print range of numbers"""
    for number in range(n):
        print(number)


def factorial(n: int) -> int:
    """This is recursive function
     to find the factorial(n)"""
    if n > 0:  # Base condition
        return factorial(n - 1) * n
    return 1


@measure_execution_time
def reverse_measure(func, *args, **kwargs):
    """This function is needed to measure execution
    time of recursive function"""
    return func(*args, **kwargs)


func_range(10)
reverse_measure(factorial, 900)
