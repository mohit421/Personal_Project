'''

'''

# Solutoom Pptimised one

# User function Template for python3
'''
Complexity Analysis

Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countPainters() function for the value of ‘mid’. Now, inside the countPainters() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
'''
class Solution:
    def largestSubSm(self, nums, largeSm):
        n = len(nums)
        sm = 0
        cnt = 1
        for i in range(n):
            if sm + nums[i] <= largeSm:
                sm += nums[i]
            else:
                sm = nums[i]
                cnt += 1
        return cnt

    def splitArray(self, nums, k):
        n = len(nums)
        if k >= n:
            return max(nums)  # Every element can be in its own subarray
        lo, hi = max(nums), sum(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            largestSm = self.largestSubSm(nums, mid)
            if largestSm > k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


    def minTime(self, arr, k):
        # code here
        return self.splitArray(arr, k)
