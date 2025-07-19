'''

'''


# Brute Force SOlution 1

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maxi = max(arr)
        cnt = 0
        n = len(arr)
        for i in range(n):
            if arr[i]<=k:
                k += 1
            else:
                break
        return k
    

# Solution 2  Optimised one using binary search

'''
Using Maths + Binary Search

Complexity Analysis

Time Complexity: O(logN), N = size of the given array.
Reason: We are using the simple binary search algorithm.

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        lo,hi = 0,n-1
        missingNum = 0
        while lo<=hi:
            mid = (lo+hi)//2
            missingNum = arr[mid] - (mid+1)
            if missingNum <k:
                lo = mid+1
            else:
                hi = mid-1
        return k + hi +1