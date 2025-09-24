'''

'''

# Using but manioulation
'''
Time = O(n), Space = O(1)
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
    


# Without using bit manipulation

# using hashmap
'''
Time = O(n), Space = O(n)
'''
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num in count:
            if count[num] == 1:
                return num



# suing maths tricks
'''
Time = O(n), Space = O(n)
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
    
# using sorting and compare
'''
Time = O(n log n), Space = O(1)
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]  # If the single number is at the end