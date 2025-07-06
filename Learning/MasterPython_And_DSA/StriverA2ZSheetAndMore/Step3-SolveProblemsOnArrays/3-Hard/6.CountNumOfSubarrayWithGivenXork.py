'''
Link:- https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1
Problem:- Count the number of subarrays with given xor K
'''

# Solution 1 Brute force
'''
omplexity Analysis

Time Complexity: O(N3) approx., where N = size of the array.
Reason: We are using three nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space.
'''
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        n = len(arr)
        cnt = 0
        for i in range(n):
            for j in range(i,n):
                xor = 0
                for l in range(i,j+1):
                    xor = xor ^ arr[l]
                if xor == k:
                    cnt += 1
        return cnt
    

# SOlution 2 Better solutton 

'''
Time Complexity: O(N2), where N = size of the array.
Reason: We are using two nested loops here. As each of them is running for N times, the time complexity will be approximately O(N2).

Space Complexity: O(1) as we are not using any extra space.
'''
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        n = len(arr)
        cnt = 0
        for i in range(n):
            xor = 0
            for j in range(i,n):
                xor = xor ^ arr[j]
                if xor == k:
                    cnt += 1
        return cnt



# Solution 3 Optimized Solution 


