'''

'''

# Brute force

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        num = abs(n)
        for i in range(1, num+1):
            if n>0:
                ans *= x
            else:
                ans = ans/x
        return ans