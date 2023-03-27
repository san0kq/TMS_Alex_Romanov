import timeit
from typing import Generator


def fib(n: int) -> Generator[int, None, None]:
    """
    Generator fibonacci numbers. n - numbers of elements you need
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib_list = []

for i in fib(100):
    fib_list.append(i)

print(fib_list)

print(timeit.timeit('for i in fib(50): fib_list.append(i)', globals=globals()))
