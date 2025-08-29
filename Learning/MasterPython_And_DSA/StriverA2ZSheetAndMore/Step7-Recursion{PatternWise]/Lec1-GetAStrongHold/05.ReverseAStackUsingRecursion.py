'''

'''


# Solution 


class Solution:
    
    def insert_at_bottom(self, St, ele):
        if not St:
            St.append(ele)
            return
        top = St.pop()
        self.insert_at_bottom(St,ele)
        St.append(top)
        
    def reverse(self,St): 
        #code here
        if St:
            temp = St.pop()
            self.reverse(St)
            self.insert_at_bottom(St,temp)
        

        