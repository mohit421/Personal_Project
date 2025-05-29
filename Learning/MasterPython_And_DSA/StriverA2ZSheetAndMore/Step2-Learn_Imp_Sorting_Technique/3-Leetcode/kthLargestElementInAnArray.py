'''
| Case            | Time Complexity              | Space Complexity |
| --------------- | ---------------------------- | ---------------- |
| Average         | `O(n)`                       | `O(n)`           |
| Worst           | `O(n^2)`                     | `O(n)`           |
| Recursive Depth | `O(log n)` avg, `O(n)` worst |                  |

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