'''

'''

# SOlution 1
'''
O(N/2) for first reverse and O(N/2) for last reverse for ans
and O(2N) for stack iteration
nearly = O(3N)
Time Complexity: O(N)

Space Complexity: O(N) for using the stack
'''
class Solution:
    def infixtoPostfix(self, s):
        #code here
        def priority(op):
            if op == '+' or op == '-':
                return 1
            if op == '*' or op == '/':
                return 2
            if op == '^':
                return 3
            return 0

        st = []
        ans = ""
        
        
        for ch in s:
            if ch.isalnum():
                ans += ch
            elif ch == '(':
                st.append(ch)
            elif ch == ')':
                while st and st[-1] != '(':
                    ans += st.pop()
                st.pop()
            else:
                while st and ((priority(ch) < priority(st[-1])) or 
                (priority(ch) == priority(st[-1]) and ch!='^')):
                    ans += st.pop()
                st.append(ch)

        while st:
            ans += st.pop()
        return ans
            
            