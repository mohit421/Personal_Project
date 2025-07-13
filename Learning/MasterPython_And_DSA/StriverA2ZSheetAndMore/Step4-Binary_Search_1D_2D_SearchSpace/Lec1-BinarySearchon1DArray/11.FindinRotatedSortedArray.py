'''

'''

# Solution 1 Brute force
'''
Complexity Analysis

Time Complexity: O(N), N = size of the given array.
Reason: We have to iterate through the entire array to check if the target is present in the array.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        maxi = 6000
        for i in range(len(nums)):
            maxi = max(maxi,nums[i])
            return maxi

# Optimised Solution Solution 2
'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using binary search to find the minimum.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo,hi = 0,n-1
        ans = sys.maxsize
        while lo<=hi:
            mid = (lo+hi)//2
            if nums[lo]<=nums[mid]:
                ans = min(ans,nums[lo])
                lo = mid +1
            else:
                ans = min(ans,nums[mid])
                hi = mid-1
        return ans