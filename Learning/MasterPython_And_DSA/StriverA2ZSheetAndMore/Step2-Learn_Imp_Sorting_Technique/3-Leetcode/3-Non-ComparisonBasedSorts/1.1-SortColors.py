'''
- Time Complexity


| Step | Description                             | Time |
| ---- | --------------------------------------- | ---- |
| 1    | `max(nums)`                             | O(n) |
| 2    | Allocate `counts` array                 | O(k) |
| 3    | Count frequencies of elements           | O(n) |
| 4    | Build cumulative count (starting index) | O(k) |
| 5    | Create sorted output list               | O(n) |
| 6    | Place elements in sorted list           | O(n) |
| 7    | Copy sorted list back to `nums`         | O(n) |


- Space Complexity:- 


| Structure    | Size  | Space |
| ------------ | ----- | ----- |
| `counts`     | k + 1 | O(k)  |
| `sorted_lst` | n     | O(n)  |

-----------

 Special Case: sortColors for Only 0, 1, 2 (as per LeetCode problem)
If you're using this code for the classic LeetCode 75 - Sort Colors problem (which contains only 0s, 1s, and 2s), then:

k = 2, so k is constant

Therefore:

Time Complexity = O(n)

Space Complexity = O(n)
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = max(nums)
        counts = [0]*(k+1)
        for elem in nums:
            counts[elem] += 1
        
        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count
        
        sorted_lst = [0]*len(nums)
        for elem in nums:
            sorted_lst[counts[elem]] = elem
            counts[elem] += 1
            
        for i in range(len(nums)):
            nums[i] = sorted_lst[i]
        
        