

# Solution 1
'''
Time complexity: O(n 
2
 ∗log(n)). Space complexity: O(n).
'''
# Basic Brute Force
class Solution:
    def check(self, nums: List[int]) -> bool:
        return any(nums[i:]+nums[:i]==sorted(nums) for i in range(len(nums)))
    

# Soplution 2

class Solution:
    def check(self, nums: List[int]) -> bool:
        x = 0
        l = nums[0]
        n = len(nums)
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                x += 1
        return x<=1
    

'''
Time complexity: O(n 
2
 ). Space complexity: O(n).
'''

class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i-1]>nums[i] for i in range(len(nums)))<2