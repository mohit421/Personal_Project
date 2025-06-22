'''

'''

# Solution 1 :- Brute force using two for loops




# SOlution 2 : Better approach using hashing

'''
| Line                      | Operation                 | Time Complexity  |
| ------------------------- | ------------------------- | ---------------- |
| `for i in range(n)`       | Loop over `n` elements    | **O(n)**         |
| `temp = target - nums[i]` | Constant-time subtraction | **O(1)**         |
| `if temp in di:`          | Dictionary lookup         | **O(1)** average |
| `di[nums[i]] = i`         | Dictionary insert         | **O(1)** average |



| Metric               | Value |
| -------------------- | ----- |
| **Time Complexity**  | O(n)  |
| **Space Complexity** | O(n)  |

'''


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}  # Use regular dict instead of defaultdict

        for i, num in enumerate(nums):
            temp = target - num
            if temp in di:
                return [di[temp], i]  # Return earlier index first
            di[num] = i

        return [-1, -1]  # In case no solution is found (not expected per problem)


# Another version of above code

from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = defaultdict(int)  # Correctly initialized with a default factory

        for i, num in enumerate(nums):
            temp = target - num
            if temp in di:
                return [di[temp], i]  # Return the earlier index first
            di[num] = i  # Store the current number and its index

        return [-1, -1]  # In case no pair is found (unlikely in valid inputs)

                         
# Optimised approach using two pointer


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store numbers with original indices
        nums_with_index = [(num, idx) for idx, num in enumerate(nums)]

        # Sort the list based on numbers
        nums_with_index.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            curr_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if curr_sum == target:
                # Return original indices
                return sorted([nums_with_index[left][1], nums_with_index[right][1]])
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]  # No valid pair found
