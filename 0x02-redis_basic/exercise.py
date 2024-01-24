#!/usr/bin/env python3
"""
Writing strings to Redis store
"""

import redis
from typing import Union
import uuid


class Cache:
    """ 
    Class defination
    """
    def __init__(self):
        """
        Initialize class
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis storage and return string
            Args:
                data: data to store
            Return:
                string representing key
        """
        key = str(uuid.uuid4())
        self.__redis.set(key, data)

        return key
