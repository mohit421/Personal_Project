''''

'''

# Using left shift operator

class Solution:
    def checkKthBit(self, n, k):
        # code here
        x = 1<<k
        if n&x != 0:
            return True
        return False
    


# One lineer

class Solution:
    def checkKthBit(self, n, k):
        # code here

        if (n&(1<<k)) != 0:
            return True
        return False
    

# Using right shift operator 

class Solution:
    def checkKthBit(self, n, k):
        # code here

        if ((n>>k)&1) != 0:
            return True
        return False

