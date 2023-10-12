from typing import Union, Callable, TypeVar, ParamSpec, Any

from .caches import SimpleCache, TTLCache, FIFOCache, LRUCache

RT = TypeVar('RT')
P = ParamSpec('P')


def cached(cache: Union[TTLCache, SimpleCache, FIFOCache, LRUCache]) -> \
        Callable[[Callable[P, RT]], Callable[P, Any]]:
    if not isinstance(cache, (SimpleCache, TTLCache, FIFOCache, LRUCache)):
        raise TypeError('Сache should only be an instance of class '
                        '(SimpleCache, TTLCache, FIFOCache, LRUCache)')

    def inner(func: Callable[P, RT]) -> Callable[P, Any]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            cache_key = (args, tuple(kwargs.values()))
            if cache_key not in cache.cache():
                cache.append(cache_key=cache_key, value=func(*args, **kwargs))
            return cache.get(cache_key=cache_key)
        return wrapper
    return inner
