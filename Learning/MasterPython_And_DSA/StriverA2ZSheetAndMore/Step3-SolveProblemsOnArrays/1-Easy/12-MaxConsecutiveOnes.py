'''
Problem:- https://leetcode.com/problems/max-consecutive-ones/
'''

# Solution 1
'''
Time Complexity: O(N) since the solution involves only a single pass.

Space Complexity: O(1) because no extra space is used.
'''

# Solution 1

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCnt = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt += 1
            else:
                cnt = 0
            maxCnt = max(maxCnt,cnt)
        return maxCnt
            

# solution 2

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCnt = 0
        cnt = 0
        for num in nums:
            if num:
                cnt += 1
            else:
                cnt = 0
            maxCnt = max(maxCnt,cnt)
        return maxCnt

            


