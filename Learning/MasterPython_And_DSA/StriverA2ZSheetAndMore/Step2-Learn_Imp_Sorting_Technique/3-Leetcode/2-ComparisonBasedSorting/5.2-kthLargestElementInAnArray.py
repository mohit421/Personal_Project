'''
| Case            | Time Complexity              | Space Complexity |
| --------------- | ---------------------------- | ---------------- |
| Average         | `O(n)`                       | `O(n)`           |
| Worst           | `O(n^2)`                     | `O(n)`           |
| Recursive Depth | `O(log n)` avg, `O(n)` worst |                  |



This is a variation of Quickselect, which is efficient for finding the k-th largest/smallest element.

The average time complexity is O(n).

It avoids sorting the whole list (which takes O(n log n)).

- Final Recursion Tree:

        findKthLargest([3,2,3,1,2,4,5,5,6], 4)
        └── pivot = 3
            left = [4,5,5,6], recurse with k=4
            └── pivot = 5
                left = [6], mid = [5,5], right = [4], recurse right with k=1
                └── pivot = 4
                    mid = [4], return 4

'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:    
            return None
        
        pivot = random.choice(nums)
#       Partition into threee groups

        left = [i for i in nums if i > pivot]      # larger than pivot
        mid = [i for i in nums if i == pivot]      # equal to pivot
        right = [i for i in nums if i < pivot]     # smaller than pivot
        
        L,M = len(left), len(mid)
        
        if k<=L:
            return self.findKthLargest(left,k)
        elif k>L+M:
            return self.findKthLargest(right,k-L-M)
        else:
            return mid[0]