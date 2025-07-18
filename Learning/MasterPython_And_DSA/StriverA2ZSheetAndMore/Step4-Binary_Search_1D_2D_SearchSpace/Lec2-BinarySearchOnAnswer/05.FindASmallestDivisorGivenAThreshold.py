'''

'''


# Solution 1 Brute Force
'''
Complexity Analysis

Time Complexity: O(max(arr[])*N), where max(arr[]) = maximum element in the array, N = size of the array.
Reason: We are using nested loops. The outer loop runs from 1 to max(arr[]) and the inner loop runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        
        maxi = max(nums)
        for d in range(1,maxi+1):
            sum = 0
            for i in range(n):
                sum += math.ceil(nums[i]/d)
            if sum<=threshold:
                return d
        return -1



# SOlution 2 
'''
Complexity Analysis

Time Complexity: O(log(max(arr[]))*N), where max(arr[]) = maximum element in the array, N = size of the array.
Reason: We are applying binary search on our answers that are in the range of [1, max(arr[])]. For every possible divisor ‘mid’, we call the sumByD() function. Inside that function, we are traversing the entire array, which results in O(N).

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        
        maxi = max(nums)
        lo,hi = 1,maxi+1
        ans = 0
        while lo<=hi:
            mid = (lo+hi)//2
            sum = 0
            for i in range(n):
                sum += math.ceil(nums[i]/mid)
            if sum<=threshold:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans