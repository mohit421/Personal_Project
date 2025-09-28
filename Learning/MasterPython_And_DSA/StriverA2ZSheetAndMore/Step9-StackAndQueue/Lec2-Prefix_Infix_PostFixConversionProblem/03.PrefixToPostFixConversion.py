'''
tC:- O(2N)
SC:- O(N)
'''

#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        n = len(pre_exp)
        i = n-1
        st = []
        while i>=0:
            if pre_exp[i].isalnum():
                st.append(pre_exp[i])
            else:
                tp1 = st.pop()
                tp2 = st.pop()
                post_exp = tp1 + tp2 + pre_exp[i]
                st.append(post_exp)
            
            i -= 1
        return st[-1]f