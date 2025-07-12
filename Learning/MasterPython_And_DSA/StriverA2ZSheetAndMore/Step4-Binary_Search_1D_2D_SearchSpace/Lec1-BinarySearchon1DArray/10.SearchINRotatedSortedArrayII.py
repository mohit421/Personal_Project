'''

'''

# Solution 1 Brute force

'''
This pass all test cases

'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return True
        return False
    

# Optimized Solution :-
'''
Complexity Analysis

Time Complexity: O(logN) for the best and average case. O(N/2) for the worst case. Here, N = size of the given array.
Reason: In the best and average scenarios, the binary search algorithm is primarily utilized and hence the time complexity is O(logN). However, in the worst-case scenario, where all array elements are the same but not the target (e.g., given array = {3, 3, 3, 3, 3, 3, 3}), we continue to reduce the search space by adjusting the low and high pointers until they intersect. This worst-case situation incurs a time complexity of O(N/2).

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        lo,hi = 0, n-1

        while lo<=hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] and nums[mid] == nums[hi]:
                lo += 1
                hi -= 1

            elif nums[lo]<=nums[mid]:
                if nums[lo]<=target and target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if nums[mid] < target and target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
        return False