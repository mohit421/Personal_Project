'''

'''

# Brute force
'''
Time Complexity: O(N)

Space Complexity: O(1)
'''
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
    
# Optimal soltuion 
'''
Time Complexity: O(log n)

Space Complexity: O(1)
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        neg = n < 0
        n = abs(n)
        ans = 1
        while n>0:
            if n%2==1:
                ans = ans*x
                n = n-1
            else:
                x = x*x
                n = n//2
        
        return ans if not neg else 1/ans
