class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            min_idx = i
            for j in range(i+1,n):
                if nums[j]<nums[min_idx]:
                    min_idx = j
            
            nums[i], nums[min_idx] =  nums[min_idx], nums[i]
        