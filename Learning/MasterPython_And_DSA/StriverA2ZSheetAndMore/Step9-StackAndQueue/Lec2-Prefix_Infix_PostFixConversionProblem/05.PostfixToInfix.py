'''

'''

#User function Template for python3
'''
O(N) in worst case take O(N) for adding string
O(N) for while loops
TC: O(2N)
SC:- O(N)
'''
class Solution:
    def postToInfix(self, postfix):
        # Code here
        i = 0
        st = []
        while i< len(postfix):
            if postfix[i].isalnum():
                st.append(postfix[i])
            else:
                tp1 = st.pop()
                tp2 = st.pop()
                infix = '(' + tp2 + postfix[i] + tp1 + ')'
                st.append(infix)
                
            i += 1
        
        return st[-1]
                