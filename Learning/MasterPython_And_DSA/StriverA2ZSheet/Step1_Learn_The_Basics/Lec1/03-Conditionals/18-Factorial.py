# Problem Link:- https://www.geeksforgeeks.org/problems/factorial-1598335080--125944/1?&selectedLang=python3

n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)

# Soluition 2

import math

def factorial_math(n):
    return math.factorial(n)

# Solution 3 Using functools.reduce() and range()

from functools import reduce

def factorial_reduce(n):
    return 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1))

# Solution 4

def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
