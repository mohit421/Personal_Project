class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        ans = 0
        nums.sort()
        mx = float(-inf)
        for i in range(1,len(nums)):
            diff = abs(nums[i]-nums[i-1])
            if mx<diff:
                mx = diff
        return mx