'''
Complexity Analysis

Time Complexity: O(N*logN)

Space Complexity: O(1)
'''

# Brute force

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return nums.sort()



# Solution 2
'''
Complexity Analysis

Time Complexity: O(N) + O(N), where N = size of the array. First O(N) for counting the number of 0’s, 1’s, 2’s, and second O(N) for placing them correctly in the original array.

Space Complexity: O(1) as we are not using any extra space.
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0,cnt1,cnt2 = 0,0,0
        n = len(nums)
        for i in range(n):
            if nums[i]==0:
                cnt0 += 1
            elif nums[i]==1:
                cnt1 += 1
            else:
                cnt2 += 1
        for i in range(cnt0):
            nums[i] = 0
        for i in range(cnt0,cnt0+cnt1):
            nums[i] = 1
        for i in range(cnt0+cnt1,n):
            nums[i] = 2
        return nums