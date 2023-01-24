from random import randint
from collections import Counter
import timeit

list_1 = [randint(1, 5) for i in range(10)]  # List with random elements


def count_dupl(list_: list) -> dict:
    """This is function to counting
    duplicate elements in list"""
    result = {}
    for number in list_:
        if number not in result:
            result[number] = 1
        else:
            result[number] += 1
    return result


def count_dupl2(list_: list) -> dict:
    """This is function to counting
    duplicate elements in list by Counter"""
    return dict(Counter(list_))


print(list_1)
print(count_dupl(list_1))
print(count_dupl2(list_1))

print(timeit.timeit('count_dupl(list_1)', globals=globals()))  # Faster
print(timeit.timeit('count_dupl2(list_1)', globals=globals()))
