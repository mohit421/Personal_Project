'''

'''

# SOlution 1

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        subset_len = 1<<l
        ans = []
        for i in range(subset_len):
            lst = []
            for j in range(l):
                if i & (1<<j):
                    lst.append(nums[j])
            ans.append(lst)
        return ans