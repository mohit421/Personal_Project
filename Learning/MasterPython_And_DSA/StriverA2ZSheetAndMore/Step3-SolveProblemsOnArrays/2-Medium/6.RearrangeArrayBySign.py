'''

'''

# SOlution 1 Brute Force

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        pos = []
        neg = []
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        for i in range(len(pos)):
            nums[2*i] = pos[i]
        for i in range(len(neg)):
            nums[2*i+1] = neg[i]
        return nums