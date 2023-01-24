dict_1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


def reverse_dict(dict_: dict) -> dict:
    """Reverse a dictionary: key > value, value > key"""
    new_dict = {v: k for k, v in dict_.items()}
    return new_dict


print(reverse_dict(dict_1))
