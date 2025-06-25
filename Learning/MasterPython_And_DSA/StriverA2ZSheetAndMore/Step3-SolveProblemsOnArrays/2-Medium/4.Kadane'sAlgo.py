'''
Link:- https://leetcode.com/problems/maximum-subarray/


Kadane's Algorithm | Maximum Subarray Sum | Finding and Printing
'''

# Solution 1 Brute force
'''
Complexity Analysis

Time Complexity: O(N3), where N = size of the array.
Reason: We are using three nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space.
'''

import sys

def maxSubarraySum(nums, n):
    maxi = -sys.maxsize - 1  # maximum sum

    for i in range(n):
        for j in range(i, n):
            # subarray = arr[i.....j]
            summ = 0

            # add all the elements of subarray:
            for k in range(i, j+1):
                summ += nums[k]

            maxi = max(maxi, summ)

    return maxi

# Solution 2 Better solution

'''
Time Complexity: O(N2), where N = size of the array.
Reason: We are using two nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space.
'''
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize - 1 # maximum sum
        n = len(nums)
        for i in range(n):
            sum = 0
            for j in range(i, n):
                # current subarray = arr[i.....j]

                #add the current element arr[j]
                # to the sum i.e. sum of arr[i...j-1]
                sum += nums[j]

                maxi = max(maxi, sum) # getting the maximum

        return maxi
    

# Solution 3 Optimised Approach Kadane's Algorithm

'''
Complexity Analysis

Time Complexity: O(N2), where N = size of the array.
Reason: We are using two nested loops, each running approximately N times.

Space Complexity: O(1) as we are not using any extra space.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize - 1 # maximum sum
        n = len(nums)
        sm = 0
        for i in range(n):
            if sm<0:
                sm = 0
            sm += nums[i]
            maxi = max(maxi,sm)
        return maxi



# Follow up question interviewer might ask

'''
Print any of subarray which will give maximum sum



Time Complexity: O(N), where N = size of the array.
Reason: We are using a single loop running N times.

Space Complexity: O(1) as we are not using any extra space.
'''
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize - 1 # maximum sum
        n = len(nums)
        sm = 0
        ansStart, ansEnd = -1,-1
        for i in range(n):
            if sm == 0: 
                start = i
            sm += nums[i]
            if sm> maxi:
                maxi = sm
                ansStart = start 
                ansEnd = i
            if sm<0:
                sm = 0
        return [ansStart,ansEnd]


