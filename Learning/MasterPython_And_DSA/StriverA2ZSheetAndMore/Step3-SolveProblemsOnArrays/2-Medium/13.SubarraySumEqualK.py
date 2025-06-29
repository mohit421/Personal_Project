'''
Link:- https://leetcode.com/problems/subarray-sum-equals-k/submissions/1680674324/
Problem:- subarray-sum-equals-k
'''

# Solution 1  Brute force
'''
Time Complexity: O(N3), where N = size of the array.
Reason: We are using three nested loops here. Though all are not running for exactly N times, the time complexity will be approximately O(N3).

Space Complexity: O(1) as we are not using any extra space.
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                sum = 0
                for m in range(i,j+1):
                    sum += nums[m]
                if  sum==k:
                    cnt += 1
        return cnt
    


# Solution 2 better approach

'''
Time Complexity: O(N2), where N = size of the array.
Reason: We are using two nested loops here. As each of them is running for exactly N times, the time complexity will be approximately O(N2).

Space Complexity: O(1) as we are not using any extra space.
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum += nums[j]
                if  sum==k:
                    cnt += 1
        return cnt
    


# Solution 3 Optimal 
#  Prefix sum 

'''

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        mpp = defaultdict(int)
        prefixSum = 0
        mpp[0] = 1

        for i in range(n):
            prefixSum += nums[i]
            diff = prefixSum - k
            cnt += mpp[diff]
            mpp[prefixSum] += 1
        return cnt
        


# Solution 4 Optimal 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        currSum = 0
        prefixSum = {0:1}

        for n in nums:
            currSum += n
            diff = currSum - k
            cnt += prefixSum.get(diff,0)

            prefixSum[currSum] = 1+ prefixSum.get(currSum,0)
        return cnt
        
