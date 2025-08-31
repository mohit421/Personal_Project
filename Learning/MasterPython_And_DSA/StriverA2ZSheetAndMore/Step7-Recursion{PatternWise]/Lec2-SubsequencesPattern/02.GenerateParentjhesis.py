'''

'''


# Solution recursive

'''
TIme Complexity:- O((4^n)/(N^(3/2)))
SC:- O(Cn * n)
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        res = []
        def validParenthesis(openP, closedP):
            if openP == closedP==n:
                res.append("".join(lst))
                return
            if openP < n:
                lst.append("(")
                validParenthesis(openP+1, closedP)
                lst.pop()
            if closedP < openP:
                lst.append(")")
                validParenthesis(openP, closedP+1)
                lst.pop()
            
        validParenthesis(0,0)
        return res
    


# Soplution 2

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def validP(curr, openP, closeP):
            if len(curr) == 2*n:
                res.append(curr)
                return
            
            if openP < n:
                validP(curr + "(", openP + 1, closeP)
            if closeP < openP:
                validP(curr + ")", openP, closeP+1)
        
        validP("", 0,0)
        return res