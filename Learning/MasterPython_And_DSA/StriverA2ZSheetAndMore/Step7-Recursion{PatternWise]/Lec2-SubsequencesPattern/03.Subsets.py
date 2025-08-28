'''

'''


# Solution 
'''
✅ Final Answer

Time Complexity: O(n*2^n)
Space Complexity:  O(n*2^n)
O(n) recursion stack
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i:int, lst: List[int]):
            if i==len(nums):
                res.append(lst[:])
                return
            
            lst.append(nums[i])
            helper(i+1, lst)
            lst.pop()
            helper(i+1, lst)

        helper(0, [])
        return res