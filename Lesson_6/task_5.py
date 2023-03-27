from collections import Counter
from random import randint
from time import time
from typing import Callable, ParamSpec, TypeVar

RT = TypeVar('RT')
P = ParamSpec('P')


def measure_execution_time(func: Callable[..., RT]) -> Callable[..., RT]:
    """Decorator to measure execution time """
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT:
        start = time()
        result = func(*args)
        end = time()
        print(f'Скорость выполнения: {end - start:.7f} sec.')
        return result
    return wrapper


@measure_execution_time
def count_dupl(list_: list[int]) -> dict[int, int]:
    """This is function to counting
    duplicate elements in list"""
    result = {}
    for number in list_:
        if number not in result:
            result[number] = 1
        else:
            result[number] += 1
    return result


@measure_execution_time
def count_dupl2(list_: list) -> dict:
    """This is function to counting
    duplicate elements in list by Counter"""
    return dict(Counter(list_))


list_1 = [randint(1, 5) for i in range(10)]

count_dupl(list_1)  # It's executing 9 times faster
count_dupl2(list_1)
