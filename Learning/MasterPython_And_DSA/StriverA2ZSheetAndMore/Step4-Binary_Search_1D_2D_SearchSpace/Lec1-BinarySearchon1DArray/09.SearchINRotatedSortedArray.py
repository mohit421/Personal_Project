'''

'''

# Solution 1

'''
Step 1: Find the Pivot (Smallest Element)
Do a binary search to find the index of the smallest value, which is the rotation point.

If nums[mid] > nums[right], pivot is to the right of mid.

If nums[mid] <= nums[right], pivot is to the left or at mid.

Step 2: Do Normal Binary Search Adjusted by Pivot
Adjust the mid index with:
realMid = (mid + pivot) % len(nums)

Compare nums[realMid] to target and proceed as normal.


Time Complexity:
Finding pivot: O(log n)

Adjusted binary search: O(log n)

✅ Total: O(log n)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo,hi = 0,n-1
        while lo<hi:
            mid = (lo+hi)//2
            if nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi = mid
        pivot = lo
        lo,hi=0,n-1
        while lo<=hi:
            mid = (lo+hi)//2
            realMid = (mid+pivot)%n
            if nums[realMid] ==target:
                return realMid
            elif nums[realMid] <target:
                lo = mid+1
            else:
                hi = mid -1
        return -1
    

# Solution 2 using binaryh search
'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are using binary search to search the target.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo,hi = 0, n-1
        while lo<=hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            
            if nums[lo]<=nums[mid]:
                if nums[lo]<=target and target <= nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if nums[mid] <= target and target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
        return -1