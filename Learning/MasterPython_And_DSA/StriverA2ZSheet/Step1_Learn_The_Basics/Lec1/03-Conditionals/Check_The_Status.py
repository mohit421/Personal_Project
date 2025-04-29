# Problem Link :- https://www.geeksforgeeks.org/problems/check-the-status/1?&selectedLang=python3

# Solution 1

class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if((a>=0 and b<0 and flag==False) or (a<0 and b>=0 and flag==False) or (a<0 and b<0 and flag==True)  ):
            return True
        else:
            return False
