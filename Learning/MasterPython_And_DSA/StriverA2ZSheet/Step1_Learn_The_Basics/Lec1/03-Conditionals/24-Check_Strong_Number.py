# Problem Link: https://www.geeksforgeeks.org/problems/strong-numbers3315/1?&selectedLang=python3


# SOlution 1
class Solution:
    def isStrong(self, N):
        # code here 
        original = N
        total = 0
        while N>0:
            dig = N%10
            total += math.factorial(dig)
            N //= 10
        return 1 if total == original else 0

# Solution 2

'''
Precomputed Factorials (Faster for Repeated Calls)
'''
class Solution:
    def isStrong(self, N):
        # code here 
        factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        original = N
        total = 0
        while N > 0:
            total += factorials[N % 10]
            N //= 10
        return 1 if total == original else 0


# Solution 3

import math
'''
 One-liner Using List Comprehension and math.factorial

'''
class Solution:
    def isStrong(self, N):
        return 1 if sum([math.factorial(int(d)) for d in str(N)]) == N else 0


# Solution 4  Recursive Version

import math

class Solution:
    def factorial_sum(self, n):
        if n == 0:
            return 0
        return math.factorial(n % 10) + self.factorial_sum(n // 10)

    def isStrong(self, N):
        return 1 if self.factorial_sum(N) == N else 0
