
# Brute Force


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = []
        count = 0
        for i in range(n):
            if nums[i] != 0:
                arr.append(nums[i])
            else:
                count += 1
        zero = [0]*count
        for i in range(count):
            arr.append(0)
        for i in range(n):
            nums[i] = arr[i]
        

# Optimised code 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                
        