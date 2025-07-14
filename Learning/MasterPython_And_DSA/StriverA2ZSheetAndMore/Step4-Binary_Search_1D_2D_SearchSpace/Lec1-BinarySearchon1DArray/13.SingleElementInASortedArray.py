'''

'''


# Solution 1  Brute force
'''
Complexity Analysis

Time Complexity: O(N), N = size of the given array.
Reason: We are traversing the entire array.

Space Complexity: O(1) as we are not using any extra space.
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(n):
            if i==0:
                if nums[i] != nums[i+1]:
                    return nums[i]
            elif i==n-1:
                if nums[i] != nums[i-1]:
                    return nums[i]
            else:
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    return nums[i]

# Solution 2 Brute for ce

class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n = len(arr)  # Size of the array
        ans = 0
        # XOR all the elements
        for i in range(n):
            ans = ans ^ arr[i]
        return ans

# Solution 3 Usinfg Binary Search

'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are not using any extra space.
'''


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        
        lo,hi = 1, n-2
        while lo<=hi:
            mid = (lo+hi)//2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if mid%2==1 and nums[mid] == nums[mid-1] or (mid%2==0 and nums[mid] == nums[mid+1]):
                lo = mid+1
            else:
                hi = mid-1
        return -1