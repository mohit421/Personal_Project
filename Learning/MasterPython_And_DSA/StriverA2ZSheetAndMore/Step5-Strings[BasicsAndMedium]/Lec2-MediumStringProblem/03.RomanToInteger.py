'''

'''

# Optimised solition
'''
TC:- O(N)
SC:- O(1)
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        # largest to smallest: add them up
        # smallest to largest: subtract them
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 
        'D':500,'M':1000, None: 0}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res



''''

'''

# Optimised one
'''
TC:- O(N)
SC:- O(1)
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        # largest to smallest: add them up
        # smallest to largest: subtract them
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 
        'D':500,'M':1000, None: 0}
        res = 0
        s = s.replace('IV',"IIII").replace("IX","VIIII")
        s = s.replace('XL',"XXXX").replace("XC","LXXXX")
        s = s.replace('CD',"CCCC").replace("CM","DCCCC")
        for ch in s:
            res += roman[ch]
        return res
