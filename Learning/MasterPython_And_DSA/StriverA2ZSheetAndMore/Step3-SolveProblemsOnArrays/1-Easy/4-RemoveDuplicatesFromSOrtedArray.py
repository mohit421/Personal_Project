# Solution 1
'''
Complexity Analysis

Time Complexity: O(N)

Space Complexity: O(1)
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1

        
            

# Solution 2
'''
Time complexity:
O(n)

Iterating through the list takes O(n).
Inserting into and checking the dictionary takes O(1) on average, repeated n times.
Clearing the list and appending back k (≤ n) unique elements takes O(n) in the worst case.
Space complexity:
O(n)

In the worst case, all elements are unique, and we store them in a dictionary which uses O(n) extra space.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
        nums.clear()
        for i in res:
            nums.append(i)
        return len(nums)
        

# Solution 3

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        prev_num = None
        i = 0
        count_uniq_nums = 0
        while (i<len_nums):
            num = nums[i]
            if prev_num is None or num != prev_num:
                nums[count_uniq_nums] = num
                count_uniq_nums += 1

            prev_num = num
            i += 1
        return count_uniq_nums
        
            

# Solution 4
'''
| Method                           | Preserves Order | In-place | Time       | Space |
| -------------------------------- | --------------- | -------- | ---------- | ----- |
| Two-pointer (best for sorted)    | ✅ Sorted        | ✅ Yes    | O(n)       | O(1)  |
| `sorted(set(arr))`               | ✅ Sorted        | ❌ No     | O(n log n) | O(n)  |
| Loop with `set` (original order) | ✅ Original      | ✅ Yes    | O(n)       | O(n)  |

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_sorted = sorted(set(nums))  # removes duplicates and sorts
        for i in range(len(unique_sorted)):
            nums[i] = unique_sorted[i]     # write back to nums
        return len(unique_sorted)