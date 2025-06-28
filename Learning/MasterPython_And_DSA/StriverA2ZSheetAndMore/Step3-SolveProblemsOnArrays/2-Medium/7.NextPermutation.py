'''
Problem:- Next Permutation
link:- https://leetcode.com/problems/next-permutation/description/
'''

# Solution 1

# Brute force approach

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prem = [[]]
        
        for n in nums:
            new_prem = []
            for p in prem:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    new_prem.append(p_copy)

            prem = new_prem   
        # Remove duplicates by converting to set of tuples, then sort
        prem_tuples = sorted(set(tuple(p) for p in prem))
        idx = prem_tuples.index(tuple(nums))
        next_prem = prem_tuples[(idx + 1) % len(prem_tuples)]

        for i in range(len(nums)):
            nums[i] = next_prem[i]                 
    

# Solution 2

# Using Itertools inbuilt  function
'''
Example Input:
nums = [1, 1, 5]

Code Breakdown:
1. 
from itertools import permutations
:- This imports the built-in function to generate all permutations of a list.


2. 
perms = sorted(set(permutations(nums)))
:- 
- permutations(nums) generates all possible arrangements (even with duplicates).

- set(...) removes duplicate tuples (since nums contains duplicate elements).

- sorted(...) sorts these permutations lexicographically.


For nums = [1, 1, 5]:
All permutations are:

(1, 1, 5)
(1, 5, 1)
(1, 1, 5)   ← duplicate
(1, 5, 1)
(5, 1, 1)
(5, 1, 1)

After removing duplicates and sorting:

perms = [
    (1, 1, 5),  # index 0
    (1, 5, 1),  # index 1
    (5, 1, 1)   # index 2
]

3. 
idx = perms.index(tuple(nums))

tuple(nums) turns nums = [1, 1, 5] into (1, 1, 5)

.index(...) finds the index of the current permutation in the sorted list.
"
idx = 0
next_perm = perms[(idx + 1) % len(perms)]
"

Get the next permutation in the list

% len(perms) makes sure that if idx is the last one, it wraps around to index 0.
4.

next_perm = perms[1] = (1, 5, 1)


5.
for i in range(len(nums)):
    nums[i] = next_perm[i]

This modifies the input list nums in-place, as required by LeetCode.

Final resul:-
nums = [1, 5, 1]  ✅


'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from itertools import permutations
        perms = sorted(set(permutations(nums)))
        idx = perms.index(tuple(nums))
        next_perm = perms[(idx + 1) % len(perms)]
        for i in range(len(nums)):
            nums[i] = next_perm[i]

