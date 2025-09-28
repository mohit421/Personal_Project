'''

'''

#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        i = 0
        n = len(post_exp)
        st = []
        while i<n:
            if post_exp[i].isalnum():
                st.append(post_exp[i])
            else:
                tp1 = st.pop()
                tp2 = st.pop()
                pre_exp =   post_exp[i] + tp2 + tp1 
                st.append(pre_exp)
       
            
            i += 1
        return st[-1]