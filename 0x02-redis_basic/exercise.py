#!/usr/bin/env python3
""" A cache class that stores an instance of the Redis client"""


import redis  # type: ignore
from typing import Union
import uuid


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    
    def store(self, data: Union[str, bytes, float, int]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key