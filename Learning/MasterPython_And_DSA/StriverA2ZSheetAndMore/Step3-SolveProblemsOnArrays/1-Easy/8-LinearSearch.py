
'''
Search Insert Position:- https://leetcode.com/problems/search-insert-position/description/
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i]> target:
                return i
            
        return i+1


# Solution 2
# Optimised above one

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
            
        return i+1
     

# Using Binary search

# Solutipon 3

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid + 1
        return left