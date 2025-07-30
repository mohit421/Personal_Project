'''
 Complexity
Time Complexity: O(n)
Space Complexity: O(n)
'''


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        balance, start = 0,0
        for i, ch in enumerate(s):
            if ch == '(':   balance += 1
            else:   balance -= 1
            if balance == 0:
                res.append(s[start+1:i])
                start = i + 1
        return ''.join(res)
    

# Other appraoich

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        balance = 0
        
        for char in s:
            if char == '(':
                if balance > 0:  # Not the outermost parenthesis
                    res.append(char)
                balance += 1
            elif char == ')':
                balance -= 1
                if balance > 0:  # Not the outermost parenthesis
                    res.append(char)
        
        return ''.join(res)
    
# Another ways


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, start, countr = [],0,0
        for ch in s:
            if ch == ')':
                countr -= 1
            if countr>0:
                res.append(ch)
            if ch == '(':
                countr += 1
        return ''.join(res)