#!/usr/bin/env python3
""" test cache results function
"""
import redis

get_page = __import__("web").get_page
client = redis.Redis()

print(get_page("http://slowwly.robertomurray.co.uk"))
print(client.get("count:http://slowwly.robertomurray.co.uk"))
