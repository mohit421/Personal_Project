'''

'''

# Solution 1 Brute force 1
'''
Complexity Analysis

Time Complexity: O(N3)

Reason: We are using 3 nested loops for finding all possible subarrays and their product.

Space Complexity: O(1)

Reason: No extra data structure was used
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float('-inf')
        for i in range(n):
            for j in range(i,n):
                prod = 1
                for k in range(i,j+1):
                    prod *= nums[k]
                maxi = max(maxi,prod)
        return maxi
    

# Solution 2 Better solutionw

'''
Complexity Analysis

Time Complexity: O(N2)

Reason: We are using two nested loops

Space Complexity: O(1)

Reason: No extra data structures are used for computation
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float('-inf')
        for i in range(n):
            prod = 1
            for j in range(i,n):
                prod *= nums[j]
                maxi = max(maxi,prod)
        return maxi


# Optimal Approach 
'''
Complexity Analysis

Time Complexity: O(N), N = size of the given array.
Reason: We are using a single loop that runs for N times.

Space Complexity: O(1) as No extra data structures are used for computation.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float('-inf')
        pre, suff = 1,1
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre = pre* nums[i]
            suff = suff*nums[n-i-1]
            maxi = max(maxi, max(pre,suff))
        return maxi
        