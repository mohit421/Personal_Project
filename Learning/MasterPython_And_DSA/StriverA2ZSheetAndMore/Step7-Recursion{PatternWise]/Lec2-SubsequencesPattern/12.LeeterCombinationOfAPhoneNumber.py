'''
https://leetcode.com/problems/combination-sum-iii/description/

'''


# Solution1


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        hshDL = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            "8":"tuv",
            '9':"wxyz"
        }
        res = []
        def helper(ind, s):
            if ind == len(digits):
                res.append(s[:])
                return
            for char in hshDL[digits[ind]]:
                helper(ind+1,s+char)
        

        helper(0,"")
        return res