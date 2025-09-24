'''

'''


# SOlution  using bit manipulation 

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res_xor = 0
        l = len(nums)
        for i in range(l):
            res_xor ^= nums[i]
        buk1, buk2 = 0,0
        rightMostBit = (res_xor &(res_xor-1))^res_xor
        for i in nums:
            if i & rightMostBit:
                buk1 ^= i
            else:
                buk2 ^= i
        return [buk1,buk2]