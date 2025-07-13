''''
Problem Link :- https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
largest-subarray-with-0-sum
'''

# Brute force 
'''
(N^3) as we have three loops for traversal
'''
class Solution:
    def maxLength(self, arr):
        # code here
        n = len(arr)
        maxi = 0
        for i in range(n):
            
            for j in range(i,n):
                sm = 0
                for k in range(i,j+1):
                    sm += arr[k]
                if sm == 0:
                    maxi = max(maxi, j-i+1)
        return maxi
        


# Better Solution

'''
(N^2) as we have two loops for traversal

Space Complexity: O(1) as we aren’t using any extra space.

Can this be done in a single traversal? Let’s check :)

'''
class Solution:
    def maxLength(self, arr):
        # code here
        n = len(arr)
        maxi = 0
        for i in range(n):
            sm = 0
            for j in range(i,n):
                sm += arr[j]
                if sm == 0:
                    maxi = max(maxi, j-i+1)
        return maxi
        

# SOluiotn 2
'''
Complexity Analysis

Time Complexity: O(NLogN), as we are traversing the array only once

Space Complexity: O(N), in the worst case we would insert all array elements prefix sum into our hashmap
'''
class Solution:
    def maxLength(self, arr):
        # code here
        n = len(arr)
        sum = 0
        maxLen = 0
        mpp = {}
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                maxLen = i+1
            else:
                if sum in mpp:
                    maxLen = max(maxLen, i- mpp[sum])
                else:
                    mpp[sum] = i
            
        return maxLen
        

