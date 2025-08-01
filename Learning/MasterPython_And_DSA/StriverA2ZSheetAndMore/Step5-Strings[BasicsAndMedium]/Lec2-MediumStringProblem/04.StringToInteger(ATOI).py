'''

'''

# Solution 1

'''
Step-by-step Analysis:
s.lstrip() — removes leading whitespace:
✅ O(n)

Sign check (+ / -) — constant-time character check:
✅ O(1)

Digit parsing loop (while i < len(s) and s[i].isdigit()):

Scans through the digits once

Each character is processed at most once
✅ O(n) in worst case (all digits)

Clamping to 32-bit range — constant time:
✅ O(1)

✅ Overall Time Complexity:
𝑂
(
𝑛
)
O(n)
​
 
✅ Space Complexity:
Using a few variables: i, res, sign → constant extra space

𝑂
(
1
)
O(1)
​

'''
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Remove leading whitespace
        if not s:
            return 0
        i,sign,res = 0,1,0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        while i<len(s) and s[i].isdigit():
            res = res*10 + int(s[i])
            i += 1
        res *= sign
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        return max(min(res,INT_MAX),INT_MIN) 
    


    # Another sol

    class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            if result * sign > 2**31 - 1:
                return 2**31 - 1
            if result * sign < -2**31:
                return -2**31
            i += 1
        
        return result * sign