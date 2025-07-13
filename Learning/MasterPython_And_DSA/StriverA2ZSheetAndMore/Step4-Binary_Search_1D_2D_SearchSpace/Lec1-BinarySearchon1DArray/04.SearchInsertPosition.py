'''

'''


# Similar to lower bound
# Solution 1 Iterative way

'''

'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low,high = 0,n-1
        ans = n
        while low<=high:
            if low>high:
                return ans
            mid = (low+high)//2
            if nums[mid]>=target:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
    


# Solution 2 Using python inbuilt func

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums,target)