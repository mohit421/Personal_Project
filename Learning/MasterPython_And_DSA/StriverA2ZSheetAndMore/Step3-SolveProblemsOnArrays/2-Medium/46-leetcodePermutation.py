# Permutation 

# Solution from neetcodeIO
'''
TC:- n! * n^2
SC:- n! * n

-------------------
| Level | List Size         | Work Done |
| ----- | ----------------- | --------- |
| n     | O(n × n!)         |           |
| n-1   | O((n-1) × (n-1)!) |           |
| n-2   | O((n-2) × (n-2)!) |           |
| ...   | ...               |           |
| 1     | O(1)              |           |

-------------

Each time we insert into a list of length k, insertion takes O(k) time (because Python lists require shifting elements).

So total work per level k includes:

Inserting into k positions

Each insertion takes O(k) (due to .insert())

That’s O(k²) work per permutation

You do this for k! permutations

So total cost at level k:
k!*k^2 = O(k!*k^2)

T(n) = sum of k=1 to k=n of (k^2 * k!) = O(n^2 * n!)



'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perm = self.permute(nums[1:])
        res = []
        for i in perm:
            for j in range(len(i)+1):

                i_copy = i.copy()
                i_copy.insert(j,nums[0])
                res.append(i_copy)
        return res
    

# Soplution 2
'''
You are building permutations incrementally. Start with an empty list, and for each number in nums, insert it into every possible position of the existing permutations.

perm = [[]]

This initializes perm with an empty list.
This means you have one permutation of zero elements, which is just [].

Example: nums = [1, 2, 3]
Let’s simulate the process step by step.

1. First iteration: n = 1
perm = [[]]
Now, you loop through perm (which has only one element: the empty list) and insert 1 at all possible positions in each permutation.

"
new_perm = []
for p in perm:  # p = []
    for i in range(len(p)+1):  # i = 0
        p_copy = p.copy()      # []
        p_copy.insert(i, 1)    # insert 1 at index 0 → [1]
        new_perm.append(p_copy)
perm = new_perm

"
Result: perm = [[1]

2. Second iteration: n = 2
perm = [[1]]
Now insert 2 at all positions in each permutation.

From [1], insert 2 at:

index 0 → [2, 1]

index 1 → [1, 2]

"
new_perm = []
for p in [[1]]:
    for i in range(2):  # len([1]) + 1 = 2
        p_copy = p.copy()
        p_copy.insert(i, 2)
        new_perm.append(p_copy)
"
Result: perm = [[2, 1], [1, 2]]

3. Third iteration: n = 3
perm = [[2, 1], [1, 2]]

Now insert 3 into each of these permutations at every possible position.

From [2, 1]:

index 0 → [3, 2, 1]

index 1 → [2, 3, 1]

index 2 → [2, 1, 3]

From [1, 2]:

index 0 → [3, 1, 2]

index 1 → [1, 3, 2]

index 2 → [1, 2, 3]

So, you get:

perm = [
    [3, 2, 1],
    [2, 3, 1],
    [2, 1, 3],
    [3, 1, 2],
    [1, 3, 2],
    [1, 2, 3]
]


return perm


This returns all permutations of [1, 2, 3]:

[
    [3, 2, 1],
    [2, 3, 1],
    [2, 1, 3],
    [3, 1, 2],
    [1, 3, 2],
    [1, 2, 3]
]


Summary:- 
| Step | Current Number | Resulting Permutations                                   |
| ---- | -------------- | -------------------------------------------------------- |
| 1    | 1              | `[[1]]`                                                  |
| 2    | 2              | `[[2,1], [1,2]]`                                         |
| 3    | 3              | `[[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]]` |


'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]

        for n in nums:
            new_perm = []
            for p in perm:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    new_perm.append(p_copy)
            perm = new_perm
        return perm




# Using Itertools solution 3


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
    