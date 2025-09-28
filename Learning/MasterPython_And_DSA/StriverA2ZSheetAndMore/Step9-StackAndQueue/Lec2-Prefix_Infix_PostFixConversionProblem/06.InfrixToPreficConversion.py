'''

'''

# SOlution 1

class Solution:
    
    def infixToPrefix(self, s):
        #code here
        def priority(op):
            if op == '^':
                return 3
            elif op in ('*','/'):
                return 2
            elif op in ('+','-'):
                return 1
            return -1
        
        s = s[::-1]
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                s[i] = ')'
            elif s[i] == ')':
                s[i] = '('
        s = "".join(s)

        st = []
        ans = ""
        
        i = 0
        while i<len(s):
            if s[i].isalnum():
                ans += s[i]
            elif s[i] == '(':
                st.append(s[i])
            elif s[i] == ')':
                while st and st[-1] != '(':
                    ans += st.pop()
                st.pop()
            else:
                if s[i] == '^':
                    while st and priority(s[i])<=priority(st[-1]):
                        ans += st.pop()
                else:
                    while st and priority(s[i])<priority(st[-1]):
                        ans += st.pop()
                st.append(s[i])
            
            i += 1
        
        while st:
            ans += st.pop()
            
        ans = ans[::-1]
        return ans
        
        
        