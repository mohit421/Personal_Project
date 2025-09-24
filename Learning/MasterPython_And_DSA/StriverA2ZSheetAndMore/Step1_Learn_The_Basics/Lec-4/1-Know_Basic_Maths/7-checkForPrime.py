'''

'''

# Solution 1  Brute Force

class Solution:
    def isPrime(self, n):
        # code here
        for i in range(2,n):
            if n%i==0:
                return False
        return True


# Soltiion 2 Optimised Solution
'''
Complexity Analysis

Time Complexity: O(sqrt(N))where N is the input number. The loop iterates up to the square root of n performing constant time operations at each step.

Space Complexity : O(1) as the space complexity remains constant and independent of the input size. Only a fixed amount of memory is required to store the integer variables.
'''

import math
class Solution:
    def isPrime(self, n):
        # code here
        count = 0
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                count += 1
                if n//i != i:
                    count += 1
        if count==2:
            return True
        else:
            return False

# Optimal

class Solution:
    def isPrime(self, n):
        
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        primes = set()
        for num in nums:
            d = 2
            while d * d <= num:
                while num % d == 0:
                    primes.add(d)
                    num //= d
                d += 1
            if num > 1:
                primes.add(num)
        return len(primes)


        


        

# libraries

from sympy import factorint

def distinctPrimeFactors(nums):
    primes = set()
    for num in nums:
        primes.update(factorint(num).keys())
    return len(primes)
