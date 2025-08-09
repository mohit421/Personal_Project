'''
https://www.geeksforgeeks.org/problems/row-with-minimum-number-of-1s5430/1
'''

# Brute force

class Solution:
    def minRow(self,a):
        #code here
        ind = 0
        min_ones = sum(a[0])
        for i in range(len(a)):
            min_cnt = sum(a[i])
            if min_cnt<min_ones:
                ind, min_ones = i,min_cnt
        return ind+1
    
# If all column sorted then we can apply binary serach on that


