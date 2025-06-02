'''
Problem Link:- https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
'''

# USinf sort


class Solution:
    def largest(self, arr):
        # code here
        arr.sort()
        return arr[-1]

# max
'''
Complexity Analysis

Time Complexity: O(n)

It must look at every element once to find the maximum.
Space Complexity: O(n)
'''

class Solution:
    def largest(self, arr):
        # code here
        return max(arr)
        


# Using for loop
'''
Complexity Analysis

Time Complexity: O(N)

Space Complexity: O(1)
'''
class Solution:
    def largest(self, arr):
        # code here
        mx = -1
        for i in arr:
            if mx<i:
                mx = i
        return mx
        


