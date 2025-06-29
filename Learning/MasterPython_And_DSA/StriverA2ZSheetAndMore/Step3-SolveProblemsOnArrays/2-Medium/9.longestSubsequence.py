'''

'''

# Solution 1 :- Brute force

class Solution:

    def linearSearch(self, nums, num):
        n = len(nums)
        for i in range(n):
            if nums[i] == num:
                return True
        return False
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        longest = 1
        for i in range(n):
            x = nums[i]
            cnt = 1
            while self.linearSearch(nums,x+1):
                x += 1
                cnt += 1
            longest = max(longest, cnt)
        
        return longest


# Solution 2 Better Solution 
'''
Complexity Analysis

Time Complexity: O(NlogN) + O(N), N = size of the given array.
Reason: O(NlogN) for sorting the array. To find the longest sequence, we are using a loop that results in O(N).

Space Complexity: O(1), as we are not using any extra space to solve this problem.
'''
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        nums.sort()
        longest = 1
        lastSmaller = float('-inf')
        currCnt = 0
        for i in range(n):
            if nums[i]-1 == lastSmaller:
                cnt += 1
                lastSmaller = nums[i]
            elif nums[i] != lastSmaller:
                lastSmaller = nums[i]
                cnt = 1
            longest = max(longest,cnt)

        return longest


# Optimal SOlution Solution 3
'''
Complexity Analysis

Time Complexity: O(N) + O(2*N) ~ O(3*N), where N = size of the array.
Reason: O(N) for putting all the elements into the set data structure. After that for every starting element, we are finding the consecutive elements. Though we are using nested loops, the set will be traversed at most twice in the worst case. So, the time complexity is O(2*N) instead of O(N2).

Space Complexity: O(N), as we are using the set data structure to solve this problem.

Note: The time complexity is computed under the assumption that we are using unordered_set and it is taking O(1) for the set operations. 

If we consider the worst case the set operations will take O(N) in that case and the total time complexity will be approximately O(N2). 
And if we use the set instead of unordered_set, the time complexity for the set operations will be O(logN) and the total time complexity will be O(NlogN).
'''

'''
O(n) – Building the set:

You iterate once through the list and insert each element into a set, which takes average-case O(1) per insert → O(n) total.

O(2n) – For the outer and inner loop combined:

You iterate over each unique number in the set.

The inner while loop (to count consecutive elements) runs only when a number is the start of a sequence.

Each number in the set is visited at most once during the entire process of checking consecutive sequences.

Even though it looks like a nested loop, no number is revisited, so the total number of operations is bounded by 2n.
 Therefore:
Best/Average Case: O(n) (assuming average O(1) set operations).

Worst Case: If hash collisions occur and set lookup becomes linear: O(n²).



Python's set behaves like C++’s unordered_set, with average O(1) insert and lookup time.

In a worst-case hashing scenario, the complexity could degrade to O(n²).

If Python used something like C++’s set (which is ordered), insertions and lookups would be O(log n) and total time would be O(n log n).
TC:-
O(n) + O(2 * n) ≈ O(3n) → O(n)

'''
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        longest = 1
        st = set()
        for i in range(n):
            st.add(nums[i])
        
        for val in st:
            if val-1 not in st:
                cnt = 1
                x = val
                
                while x+1 in st:
                    x += 1
                    cnt += 1
                longest = max(longest,cnt)
        return longest

