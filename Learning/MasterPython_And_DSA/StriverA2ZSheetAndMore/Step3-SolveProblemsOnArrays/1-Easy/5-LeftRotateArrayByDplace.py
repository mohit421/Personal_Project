'''

'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==0 or k<=0:
            return
        arr = [0]*n
        for i in range(n):
            arr[i] = nums[i]
        for i in range(n):
            nums[(i+k)%n]= arr[i]


# Solution 2

'''
Manual Copy (Similar to above, with Optimization)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums_copy = nums[:]
        for i in range(n):
            nums[(i + k) % n] = nums_copy[i]



# Solution 3

'''
: Slice Assignment (Pythonic, not constant space)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k  %= n
        nums[:] = nums[-k:] + nums[:-k]


# Solution 4

'''
Reverse Method (Most Optimal, In-place, O(n) time, O(1) space)
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k  %= n
        def reverse(start,end):
            while start<end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
        
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)


# Solution 5
'''
Cyclic Replacements (Efficient In-Place Algorithm)
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k  %= n
        count = 0
        start = 0
        while count<n:
            current = start
            prev = nums[start]
            while True:
                next_idx = (current+k)%n
                nums[next_idx],prev = prev,nums[next_idx]
                current = next_idx
                count += 1
                if start == current:
                    break
            start += 1
