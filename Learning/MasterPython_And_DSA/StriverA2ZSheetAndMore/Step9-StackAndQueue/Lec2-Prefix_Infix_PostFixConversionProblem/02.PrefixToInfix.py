
'''
worst possible case for connecting all string is to O(N)
TC:- O(N) + O(N)
'''
#User function Template for python3

class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        n = len(pre_exp)
        st = []
        i = n-1
        while i>=0:
            if pre_exp[i].isalnum():
                st.append(pre_exp[i])
            else:
                tp1 = st.pop()
                tp2 = st.pop()
                infix = '(' + tp1 + pre_exp[i] + tp2 + ')'
                st.append(infix)
            
            i -= 1
        return st[-1]
            