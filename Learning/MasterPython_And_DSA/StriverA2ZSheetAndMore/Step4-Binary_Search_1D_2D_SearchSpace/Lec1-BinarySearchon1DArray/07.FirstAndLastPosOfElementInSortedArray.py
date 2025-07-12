'''

'''

# Solution 1 Brute Force

'''
Simple two traversal

TC:- O(N) + O(N) = 2*O(N)
SC:- O(1)
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first , last = -1,-1
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                first = i
                break
        for i in range(n):
            if nums[n-i-1] == target:
                last = n-i-1
                break
        return [first, last]
            

# Above using 1 traversal

class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first,last = -1, -1
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first,last]

# Solution 2 Optimised solution using Binary Search lower and upper bound
'''
TC:- O(LogN) + O(logN)
SC:- O(1)
'''

class Solution:
    def lowerBound(self, nums, low, high, target):
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                ans = mid
                high = mid-1
            elif nums[mid]<target:
                low = mid +1
            else:
                high = mid -1
        return ans

    def upperBound(self, nums, low, high,target):
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                ans = mid
                low = mid +1
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid+1
                
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low, high = 0,n-1
        first = self.lowerBound(nums,low,high,target)
        last =  self.upperBound(nums,low,high,target)
        return [first, last]
    

# Solution 3 using in built function


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        first, last = -1,-1
        first = bisect.bisect_left(nums,target)
        last = bisect.bisect_right(nums,target)
        # Check if the target actually exists in the list
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        return [first, last-1]


# Solution 4 Using one liner most optimized one

class Solution:
    def biSearch(self,nums, target):
        n = len(nums)
        lo,hi = 0,n
        while lo<hi:
            mid = (lo + hi)//2
            if nums[mid]<target:
                lo = mid+1
            else:
                hi = mid
        return lo
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = self.biSearch(nums, target)
        high = self.biSearch(nums, target + 1)

        if low < len(nums) and nums[low] == target:
            return [low, high - 1]
        return [-1, -1]


# Other easys

class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def biSearch(target):
            n = len(nums)
            lo, hi = 0, n
            while lo<hi:
                mid = (lo + hi)//2
                if nums[mid]<target:
                    lo = mid+1
                else:
                    hi = mid
            return lo
        lo = biSearch(target)
        hi = biSearch(target+1)-1
        if lo <= hi:
            return [lo, hi]
        return [-1, -1]

