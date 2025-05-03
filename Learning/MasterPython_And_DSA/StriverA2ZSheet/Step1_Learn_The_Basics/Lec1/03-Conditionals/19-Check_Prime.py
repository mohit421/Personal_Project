# Problem Link:- https://www.geeksforgeeks.org/problems/check-prime--153305/1?&selectedLang=python3

# Solution 1 Naive Approach

# Time Complexity:
# O(n) — Very inefficient for large n.



n = int(input())
def check_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(check_prime(n))


# Solution 2  Check up to √n
# If n is divisible by a number greater than √n, it must also be divisible by one smaller than √n.

# Time Complexity:
# O(√n) — Much faster.

import math

def check_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n)),2):
        if n%i==0:
            return False
    return True

# Your code here
n = int(input())
print(check_prime(n))