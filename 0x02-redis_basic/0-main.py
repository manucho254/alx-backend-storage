#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))


cache = Cache()

TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
        }

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    print(cache.get(key, fn=fn), value)
    print(type(cache.get(key, fn=fn)), type(value))
    print(cache.get(key, fn=fn) == value)
    assert cache.get(key, fn=fn) == value


# count number of function calls
cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
