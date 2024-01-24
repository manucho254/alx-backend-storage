#!/usr/bin/env python3
""" Writing strings to Redis
"""
import redis
from typing import Union
import uuid


class Cache:
    """ Cache class defination
    """
    def __init__(self):
        """ Initialize class
        """
        self.__redis = redis.Redis(decode_responses=True)
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis
            Args:
                data: data to store
            Return:
                string representing key
        """
        key: str = str(uuid.uuid4())
        self.__redis.set(key, data)

        return key
