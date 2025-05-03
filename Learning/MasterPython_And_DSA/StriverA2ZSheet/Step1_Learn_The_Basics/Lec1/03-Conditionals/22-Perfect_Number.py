# Problem Link:-

# Solution 1 Naive approach (TLE)
#  Time Complexity: O(n) — can TLE for large n
class Solution:
    def isPerfectNumber(self, n):
        # code here 
        sm  = 0
        for i in range(1,n):
            if(n%i==0):
                sm += i
        if sm ==n:
            return True
        return False
    


# Solution 2
'''
 Time Complexity:
O(√n) — much faster than the original O(n)

Efficient for all reasonable inputs

+  Logic:
If i is a factor of n, then n // i is also a factor.
So you only need to iterate from 1 to sqrt(n) and sum both i and n // i (excluding n itself).


'''
import math
class Solution:
    def isPerfectNumber(self, n):
        # code here 
        if(n<=1):
            return False
        sm  = 1
        for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                sm += i
                if i != n//i:
                    sm += n//i
        if sm ==n:
            return True
        return False

# Solution 3

import math

def is_perfect(n):
    if n <= 1:
        return False

    sm = 1  # 1 is a factor of all n > 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sm += i
            if i != n // i:
                sm += n // i
    return sm == n


# Solution 4  3. List Comprehension Approach
#  Time Complexity: O(n) — readable but not optimal
def is_perfect(n):
    return n > 1 and sum([i for i in range(1, n) if n % i == 0]) == n

# Soluton 5  Using divmod() with Symmetric Factor Sum
# TC;_ O(√n)
import math

def is_perfect(n):
    if n <= 1:
        return False

    sm = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        q, r = divmod(n, i)
        if r == 0:
            sm += i
            if i != q:
                sm += q
    return sm == n
