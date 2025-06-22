'''
Problem link:- https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1
'''

#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        i,j = 0,0
        union = []
        n1,n2 = len(a),len(b)
        while i<n1 and j<n2:
            if a[i]<=b[j]:
                if len(union)==0 or union[-1] != a[i]:
                    union.append(a[i])
                i += 1
            else:
                if len(union)==0 or union[-1] != b[j]:
                    union.append(b[j])
        
                j += 1
            
        while i<n1:
            if union[-1] != a[i]:
                union.append(a[i])
            i += 1
        
        while j<n2:
            if union[-1] != b[j]:
                union.append(b[j])
            j += 1
        
        return union
    


# Solution 2

'''
Learn more about it in heapq

'''

#User function Template for python3
from heapq import merge

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        union = []
        prev = None
        for num in merge(a, b):
            if num != prev:
                union.append(num)
                prev = num
        return union