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

We will make a custom wrapper that stores the function inputs in a memoization table
"""

def custom_cache(func):
    memo={}
    def wrapper(n):
        if n in memo:
            return memo[n]
        result=func(n)
        memo[n]=result
        return result
    return wrapper

#ok so let's try the custom version now:
@custom_cache
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))