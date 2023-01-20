from datetime import datetime
import time


def current_time() -> str:
    """This is function return format
    current time with delay 1 second"""
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


list_1 = [current_time() for _ in range(int(input('Введите кол-во элементов в списке: ')))]
print(list_1)
