'''

'''

# SOlution using bit mannipulation

#User function Template for python3

class Solution:
    def findXOR(self, l, r):
        # Code here
        ans = 0
        for i in range(l,r+1):
            ans = ans^i
        return ans