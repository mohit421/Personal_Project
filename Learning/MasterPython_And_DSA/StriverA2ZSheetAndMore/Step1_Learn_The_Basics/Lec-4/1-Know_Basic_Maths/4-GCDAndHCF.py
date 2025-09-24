'''
LCM and GCD :- https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1
'''



class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        l = []
        gcd = math.gcd(a,b)
        lcm = (a*b)//gcd
        l.append(lcm)
        l.append(gcd)
        return l
    

# Solution 2

class Solution:
    
    def compute_gcd(self,a,b):
        while b:
            a,b = b,a%b
        return a
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        gcd = self.compute_gcd(a,b)
        lcm = (a*b)//gcd
        return [lcm,gcd]

# Solution 2


class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        return [a*b // math.gcd(a,b),math.gcd(a,b)]
    

# SOlution 3

import math

def lcm_and_gcd(a, b):
    return [math.lcm(a, b), math.gcd(a, b)]


# Solution 4

class Solution:
    
    def compute_gcd(self,a,b):
        return a if b==0 else self.compute_gcd(b,a%b)
        
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        g = self.compute_gcd(a,b)
        lcm = a*b // g
        return [lcm,g]
    

# Striver solution 
# Brute force
'''
TC;- O(min(n1,n2))
'''
class Solution:
    def gcd(self, a, b):
        # code here
        gcd = 1
        for i in range(1, min(a,b)+1):
            if a%i == 0 and b%i==0:
                gcd = i
        
        return gcd
    


# 
'''
TC:- O(min(n1,n2))
'''
class Solution:
    def gcd(self, a, b):
        # code here
        gcd = 1
        for i in range(min(a,b), 0, -1):
            if a%i == 0 and b%i==0:
                gcd = i
                break
        
        return gcd
    
# Euclidean Algorithms

'''
gcd(a,b) = gcd(a-b,b) where a>b
'''

class Solution:
    def gcd(self, a, b):
        # code here
        
        while a>0 and b>0:
            if a>b:
                a = a%b
            else:
                b = b%a
        
        if a==0:
            return b
        else:
            return a
        
# -----------------------------------------------
'''
Leetcode
1979. Find Greatest Common Divisor of Array

TC:- O(logPhi(min(a,b)))
'''

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        b = min(nums)
        a = max(nums)
        ans  = 0
        while a>0 and b>0:
            if a>b:
                a = a%b
            else:
                b = b%a
        if a == 0:
            ans = b
        else:
            ans = a
        return ans   
