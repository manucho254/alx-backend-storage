#!/usr/bin/env python3
"""
Writing strings to Redis store
"""
from collections.abc import Callable
from functools import wraps
import redis
from typing import Union, Optional
import uuid


def count_calls(method: Callable):
    """ count number of calls
        Args:
            function to count number of calls
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__, 1)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
      Class defination
    """
    def __init__(self):
        """
        Initialize class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis storage and return string
            Args:
                data: data to store
            Return:
                string representing key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """ get value by key
            Args:
                key: key to find value
                fn: comversion function
            Return:
                any type
        """
        if fn:
            return fn(self._redis.get(key))

        return self._redis.get(key)

    def get_str(self, val) -> str:
        """ convert bytes to string
            Args:
                val: value to convert to string
            Return:
                value as string
        """
        return val.decode("utf-8")

    def get_int(self, val) -> int:
        """ convert bytes to int
            Args:
                val: value to convert to int
            Return:
                value as integer
        """
        return int(val.decode("utf-8"))
