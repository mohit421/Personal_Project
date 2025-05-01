# Problem link:- http://geeksforgeeks.org/problems/overlapping-rectangles1924/1?&selectedLang=python3

# Solution 1

'''
Problem Understanding:
Each rectangle is defined by:

L1 (x1, y1) and R1 (x2, y2) → top-left and bottom-right of first rectangle

L2 (x3, y3) and R2 (x4, y4) → top-left and bottom-right of second rectangle

The rectangles overlap if and only if they do NOT lie completely apart either:

to the left or right

above or below each other
'''

class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
        #code here
        if L1[1] < R2[1] or L2[1]<R1[1]:
            return 0
        elif R1[0]<L2[0] or R2[0] <L1[0]:
            return 0
        else:
            return 1