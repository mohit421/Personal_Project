# Problem Link:- 


# Solution 1  terative check
# Time Complexity :- O(n√n) worst case
n = int(input())

# Your code here
import math

def check_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def next_prime(n):
    n+=1
    while not check_prime(n):
        n+=1
    return n

print(next_prime(n))


# Solution 2
'''
 2. Use Probabilistic Primality (for large numbers)
For very large values (e.g., in cryptography), you can use Miller-Rabin primality test which is fast and probabilistic.

Example (Python pseudocode using sympy):
'''

# /Solution 3 

'''
Precomputed Prime Tables (Sieve)
If you're finding next primes repeatedly for many values up to some max N, use the Sieve of Eratosthenes:


'''