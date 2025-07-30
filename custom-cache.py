"""
manually building Python's built-in Cache decorator; automatic memoization
"""

"""
from functools import cache
@cache
def fibonacci(n):
    if n>=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
    

"""

def custom_cache(func):
    def wrapper(*args,**kwargs):
        memo={}

    return wrapper

#ok so let's try the custom version now:
@custom_cache
def fibonacci(n):
    if n>=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))