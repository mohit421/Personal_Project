'''

'''


# Solution 1
'''
TC:- O(N)
SC:- O(1)
'''

class Solution:
    # intuition behind is we have to found '(' before number and keep track of maximum '(' in the string 
    
    def maxDepth(self, s: str) -> int:
        dpt = 0
        maxi = -1
        # Traverse the string
        for ch in s:
            # if we found '(' increment dpt by 1 else decrease by 1
            if ch == '(':
                dpt += 1
            elif ch == ')':
                dpt -= 1
            # keep track of maxi '('
            maxi = max(maxi,dpt)
        return maxi
    


# SOlution 2 using stack
'''
Complexity
Time complexity: O(n)
We iterate through the string once, where n is the length of the string

Space complexity:O(1)
Only two integer variables are used, regardless of input size.
'''
class Solution:
    def maxDepth(self, s: str) -> int:
        stacks = []
        res = 0
        for char in s:
            if char == '(':
                stacks.append(char)
                res = max(res,len(stacks))
            elif char == ')':
                stacks.pop()
        return res