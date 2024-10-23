#!/usr/bin/env python3
""" A cache class that stores an instance of the Redis client"""


import redis  # type: ignore
from typing import Union, Callable, Optional
import uuid


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    
    def store(self, data: Union[str, bytes, float, int]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, int, float, bytes]]:
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)