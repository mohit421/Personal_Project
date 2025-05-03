# Problem Link: https://www.geeksforgeeks.org/problems/fibonacci-number-1605700704--152305/1?&selectedLang=python3


# Solution 1:
n = int(input())


def fibonacci(n):
    if n<0: return "Invalid input"
    if n==0:    
        return 0
    if n==1:    
        return 1
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
fib = fibonacci(n)


print(fib)

# Solution 2
'''
Constant space using Iterative approach

'''

n = int(input())

def fibonacci(n):
    if n < 0:
        return "Invalid input"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci(n))


# Solution 3

'''
Recursive Naive
'''

n = int(input())

def fibonacci(n):
    if n < 0:
        return "Invalid input"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))


# Recursive with Memoization

from functools import lru_cache

n = int(input())

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 0:
        return "Invalid input"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(n))
