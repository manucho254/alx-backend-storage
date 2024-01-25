#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
"""
import requests
from functools import wraps
from typing import Callable, Any
import redis
from datetime import timedelta


client = redis.Redis()  # new redis instance


def cache_result(func: Callable) -> Any:
    """ decorator function
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """ wrapper function to cache
            responses that expire in 10 seconds
        """
        url = args[0]
        cached_page = client.get(url)

        # send request again to url if no cache is found
        # an update info else get cached data
        if not cached_page:
            client.incr("count:{}".format(url))
            return_val = func(*args, **kwargs)
            client.setex(url, 10, return_val)
            return return_val

        return client.get(url).decode("utf-8")

    return wrapper


@cache_result
def get_page(url: str) -> str:
    """ get page data
        Args:
            url: website url
        Return:
           data from page
    """
    query = requests.get(url)

    return query.text
