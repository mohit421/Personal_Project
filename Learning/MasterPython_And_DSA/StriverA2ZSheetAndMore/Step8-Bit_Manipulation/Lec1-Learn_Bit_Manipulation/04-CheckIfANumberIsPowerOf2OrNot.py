'''

'''

# Solution
class Solution:
    def isEven (self, n):
        # code here 
        
        if n & 1:    # if last bit is 1 → odd
            return False
        else:   # if last bit is 0 → even
            return True
        


# Solution

class Solution:
    def isEven(self, n):
        return (n & 1) == 0