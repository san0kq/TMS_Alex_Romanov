import timeit

number = int(input('Введите целое число: '))

# For loop
result_for = 0
for num in range(1, number + 1):
    result_for += num**2

print(result_for)

# While loop
result_while = 0
counter = 1
while counter <= number:
    result_while += counter**2
    counter += 1

print(result_while)


# Сheck the speed of loop execution
speed_while = """\
result_while = 0
counter = 1
while counter <= number:
    result_while += counter**2
    counter += 1
"""
speed_for = """\
result_for = 0
for num in range(1, number+1):
    result_for += num**2
"""

print(timeit.timeit(speed_while, globals=globals()))
print(timeit.timeit(speed_for, globals=globals()))
