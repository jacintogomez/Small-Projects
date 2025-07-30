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
    def wrapper(*args,**kwargs):
        key=(args,frozenset(kwargs.items()))
        if key in memo:
            return memo[key]
        result=func(*args,**kwargs)
        memo[key]=result
        return result
    return wrapper

#ok so let's try the custom version now:
@custom_cache
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print('Fibonacci Result:',fibonacci(10))

#and the generic multi-input version
@custom_cache
def binomial(n,k):
    if k==0 or k==n:
        return 1
    return binomial(n-1,k-1)+binomial(n-1,k)

print('Binomial Result:',binomial(10,3))