#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
"""
import requests
from functools import wraps
from typing import Callable, Any
import redis


client = redis.Redis()  # new redis instance


def cache_result(func: Callable) -> Any:
    """ decorator function
    """
    key = func.__qualname__

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """ wrapper function to cache
            responses that expire in 10 seconds
        """
        return_val = func(*args, **kwargs)
        client.set(key, return_val, ex=10)

        return return_val

    return wrapper


def count_accessed(func: Callable) -> Any:
    """ decorator function
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """ wrapper function to count the
            number of requests made to url
        """
        client.incr("count:{}".format(args[0]))
        return func(*args, **kwargs)

    return wrapper


@count_accessed
@cache_result
def get_page(url: str) -> str:
    """ get page data
        Args:
            url: website url
        Return:
           data from page
    """
    cached_page = client.get("get_page")
    if cached_page:
        return cached_page

    query = requests.get(url)

    return query.text
