from collections import OrderedDict
from time import time
from typing import Any


class MaxSizeMixin:
    @property
    def max_size(self) -> int:
        return self._max_size

    @max_size.setter
    def max_size(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError('Mas size must be integer')
        if not 1 <= value <= 999:
            raise ValueError('Max size must be in range (1-999)')
        self._max_size = value


class SimpleCache:
    def __init__(self) -> None:
        self._cache = OrderedDict()

    def cache(self) -> OrderedDict:
        return self._cache

    def append(self, cache_key: Any, value: Any) -> None:
        self._cache[cache_key] = value

    def get(self, cache_key: Any) -> Any:
        return self._cache.get(cache_key)


class FIFOCache(SimpleCache, MaxSizeMixin):
    def __init__(self, max_size: int) -> None:
        super().__init__()
        self.max_size = max_size

    def append(self, cache_key: Any, value: Any) -> None:
        if len(self._cache) == self.max_size:
            self._cache.pop(next(iter(self._cache)))
        self._cache[cache_key] = value


class LRUCache(SimpleCache, MaxSizeMixin):
    def __init__(self, max_size: int) -> None:
        super().__init__()
        self.max_size = max_size

    def append(self, cache_key: Any, value: Any) -> None:
        if len(self._cache) == self.max_size:
            self._cache.pop(next(iter(self._cache)))
        self._cache[cache_key] = value

    def get(self, cache_key: Any) -> Any:
        self._cache.move_to_end(cache_key)
        return self._cache.get(cache_key)


class TTLCache(SimpleCache, MaxSizeMixin):
    def __init__(self, max_size: int, ttl: int) -> None:
        super().__init__()
        self.max_size = max_size
        self.ttl = ttl

    @property
    def ttl(self) -> int:
        return self._ttl

    @ttl.setter
    def ttl(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError('ttl must be integer')
        if not 5 <= value <= 86400:
            raise ValueError('ttl must be in range (5-86400).')
        self._ttl = value

    def append(self, cache_key: Any, value: Any) -> None:
        if len(self._cache) == self.max_size:
            for key in list(self._cache.keys()):
                if time() - self._cache[key][1] >= self.ttl:
                    self._cache.pop(key)
        if len(self._cache) == self.max_size:
            self._cache.pop(next(iter(self._cache)))
        self._cache[cache_key] = (value, time())

    def get(self, cache_key: Any) -> Any:
        self._cache.move_to_end(cache_key)
        return self._cache.get(cache_key)[0]
