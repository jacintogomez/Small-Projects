"""
Cache Decorator:
saves function returns in dictionary; automatic memoization for recursive calls
"""
from functools import cache
@cache
def fibonacci(n):
    if n>=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

"""
Default Dict:
dictionary with default values; immediate increments/decrements
"""
from collections import defaultdict
count=defaultdict(int)
count['a']+=1
print(count['a'])

"""
Enumerate:
iterate through iterable with both index and value
"""
l=[True,False,True]
for x,y in enumerate(l):
    print(x,' is ',y)

"""
Zip:
parallel iteration through 2 lists
"""
d=[1,2,3,4,5]
f=['a','b','c']
for x,y in zip(d,f):
    print(x,' and ',y)

"""
Any/All:
"""
nums=[2,4,6,8]
print(any(n%2==1 for n in nums))
print(all(n%2==0 for n in nums))

"""
Counter:
"""
from collections import Counter
arr=[1,2,4,3,5,4,5,6,7,8,8,7,6,5,4,4,5,5,3,3,4,5,5,5,3,3,3,4,5,4,3,2]
count=Counter(arr)
print(count)
print(count.most_common(1))

"""
Combinations:
"""
from itertools import combinations
print(list(combinations(nums,2)))