'''

'''

# Brute force

class Solution:
    def largestSubSm(self, nums: List[int], largeSm: int)-> int:
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
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k>n:
            return -1
        lo,hi = max(nums), sum(nums)

        for i in range(lo,hi+1):
            if self.largestSubSm(nums,i) == k:
                return i
        return lo
    

    # Spluition 2 Optimisec one
class Solution:
    def largestSubSm(self, nums: List[int], largeSm: int)-> int:
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
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k>n:
            return -1
        lo,hi = max(nums), sum(nums)
        while lo<=hi:
            mid = (lo+hi)//2
            LargestSm = self.largestSubSm(nums,mid)
            if LargestSm > k:
                lo  = mid+1
            else:
                hi = mid-1
        return lo