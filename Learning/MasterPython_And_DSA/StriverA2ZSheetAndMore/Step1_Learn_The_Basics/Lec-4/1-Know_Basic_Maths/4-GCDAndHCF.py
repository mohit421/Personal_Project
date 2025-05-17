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