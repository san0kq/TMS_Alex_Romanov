from typing import Union, Callable

from .caches import SimpleCache, TTLCache, FIFOCache, LRUCache


def cached(cache: Union[TTLCache, SimpleCache, FIFOCache, LRUCache]):
    if not isinstance(cache, (SimpleCache, TTLCache, FIFOCache, LRUCache)):
        raise TypeError('Сache should only be an instance of class '
                        '(SimpleCache, TTLCache, FIFOCache, LRUCache)')

    def inner(func: Callable):
        def wrapper(*args, **kwargs):
            cache_key = (args, tuple(kwargs.values()))
            if cache_key not in cache.cache():
                cache.append(cache_key=cache_key, value=func(*args, **kwargs))
            return cache.get(cache_key=cache_key)
        return wrapper
    return inner
