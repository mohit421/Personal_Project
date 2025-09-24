'''

'''

# Solution 1 Brute force

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sm = 0
        for i in range(1,num):
            if num % i==0:
                sm += i
        if sm == num:
            return True
        return False
    


# Optimal
# TC:- O(sqrt(n))
# SC:- O(1)

import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:  # 1 is not a perfect number
            return False
        sm = 1
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                sm += i
                if num//i != i:
                    sm += num//i
        if sm == num:
            return True
        return False
