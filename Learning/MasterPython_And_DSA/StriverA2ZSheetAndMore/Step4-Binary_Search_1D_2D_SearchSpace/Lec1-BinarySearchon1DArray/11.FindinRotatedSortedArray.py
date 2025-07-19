'''

'''

# Solution 1 Brute force
'''
Complexity Analysis

Time Complexity: O(N), N = size of the given array.
Reason: We have to iterate through the entire array to check if the target is present in the array.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        maxi = 6000
        for i in range(len(nums)):
            maxi = max(maxi,nums[i])
            return maxi

# Optimised Solution Solution 2
'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using binary search to find the minimum.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo,hi = 0,n-1
        ans = sys.maxsize
        while lo<=hi:
            mid = (lo+hi)//2
            if nums[lo]<=nums[mid]:
                ans = min(ans,nums[lo])
                lo = mid +1
            else:
                ans = min(ans,nums[mid])
                hi = mid-1
        return ans
    

# Solution 3Optimised sol

'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using binary search to find the minimum. 

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo,hi = 0, n-1
        ans = sys.maxsize
        while lo<=hi:
            mid = (lo +hi)//2
            if nums[lo]<=nums[hi]:
                ans = min(ans, nums[lo])
                break
            if nums[lo]<= nums[mid]:
                ans = min(ans, nums[lo])
                lo = mid +1
            else:
                ans = min(ans, nums[mid])
                hi  = mid-1
        return ans

    

# Solution 3 got this ideaf from quesrtion no 11\

class Solution:
    def findKRotation(self, arr):
        # code here
        n = len(arr)
        lo,hi = 0,n-1
        ans = sys.maxsize
        idx = -1
        while lo<=hi:
            mid = (lo+hi)//2
            if arr[lo]<=arr[hi]:
                if arr[lo]<ans:
                    idx = lo
                    ans = arr[lo]
                break
            if arr[lo]<=arr[mid]:
                if arr[lo]<ans:
                    idx = lo
                    ans = arr[lo]
                lo = mid+1
            else:
                if arr[mid]<=ans:
                    idx = mid
                    ans = arr[mid]
                hi = mid-1
        return idx
                