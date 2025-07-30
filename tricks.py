"""
Cache Decorator:
saves function inputs (keys) and return values (values) in dictionary; automatic memoization for recursive calls
"""
print('Cache Decorator')
from functools import cache
@cache
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

"""
Default Dict:
dictionary with default values; immediate increments/decrements without having to check for existence
"""
print('Default Dict')
from collections import defaultdict
count=defaultdict(int)
count['a']+=1 #'a' wasn't in the dict yet and would normally cause an error, but not with defaultdict
print(count['a'])

"""
Enumerate:
iterate through iterable with both index and value
"""
print('Enumerate')
l=[True,False,True]
for x,y in enumerate(l):
    print(x,' is ',y)

"""
Zip:
parallel iteration through 2 lists
"""
print('Zip')
d=[1,2,3,4,5]
f=['a','b','c']
for x,y in zip(d,f):
    print(x,' and ',y) #limited by shortest list

"""
Any/All:
"""
print('Any/All')
nums=[2,4,6,8]
print(any(n%2==1 for n in nums))
print(all(n%2==0 for n in nums)) #this is NOT the same as all(n for n in nums if n%2==0)

"""
Counter:
"""
print('Counter')
from collections import Counter
arr=[1,2,4,3,5,4,5,6,7,8,8,7,6,5,4,4,5,5,3,3,4,5,5,5,3,3,3,4,5,4,3,2]
count=Counter(arr)
print(count)
print(count.most_common(1)) #int input is the top n results, so 1 is the top 1, 2 would be 1 and 2 in descending order

#or put into dictionary directly
darr=defaultdict(int,Counter(arr))
print(darr)

"""
Combinations:
"""
print('Combinations')
from itertools import combinations
print(list(combinations(nums,2)))

"""
Unpacking operators * and **:
"""
print('Unpacking Operators')
# Unpacking elements
list1=[1,2,3,4,5]
print(*list1)
list2=[0,*list1,6]
print(list2)
# Unpacking key-value pairs
dic1={'A':1,'B':2,'C':3}
dic2={'D':4,'E':5,'F':6}
dic3={**dic1,**dic2}
print(dic3)
