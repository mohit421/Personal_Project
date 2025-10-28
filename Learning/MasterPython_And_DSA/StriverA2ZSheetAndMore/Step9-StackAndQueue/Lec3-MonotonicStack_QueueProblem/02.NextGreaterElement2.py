
'''

'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1]*n
        st = []
        for i in range(2*n):
            while st and nums[st[-1]] < nums[i%n]:
                nge[st.pop()] = nums[i%n]
            
            if i<n:
                st.append(i%n)
        
        return nge