'''

'''

# SOlution using bit mannipulation

'''
Complexity Analysis
Time Complexity: O(N) Traversing through all the numbers take O(N) time.

Space Complexity: O(1) Using only a couple of variables, i.e., constant space.
'''

class Solution:
    def findXOR(self, l, r):
        # Code here
        ans = 0
        for i in range(l,r+1):
            ans = ans^i
        return ans
    


# Solution 2

