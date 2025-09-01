
'''

'''





# Solution 1 Brute force approach

'''
Time Complexity: O( 2^n *(k log (x) )). 2^n  for generating every subset and k* log( x)  to insert every combination of average length k in a set of size x. After this, we have to convert the set of combinations back into a list of list /vector of vectors which takes more time.

Space Complexity:  O(2^n * k) to store every subset of average length k. Since we are initially using a set to store the answer another O(2^n *k) is also used.
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = set()
        nums.sort()
        def helper(ind: int, lst: List[int]):
            if ind == len(nums):
                res.add(tuple(lst))
                return
            lst.append(nums[ind])
            helper(ind+1, lst)
            lst.pop()
            helper(ind+1, lst)
        helper(0,[])
        for it in res:
            ans.append(list(it))
        return ans 
        
        



# Solution 2  Optimal

'''
Time Complexity: O(2^n) for generating every subset and O(k)  to insert every subset in another data structure if the average length of every subset is k. Overall O(k * 2^n).

Space Complexity: O(2^n * k) to store every subset of average length k. Auxiliary space is O(n)  if n is the depth of the recursion tree.
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        def helper(i,lst):
            if i == n:
                ans.append(lst[:])
                return
            lst.append(nums[i])
            helper(i+1, lst)
            lst.pop()
            while i+1<n and nums[i] == nums[i+1]:
                i += 1
            helper(i+1, lst)
        

        helper(0,[])
        return ans
    

# Solution 3 Optimal 

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []


        def findSubsets(ind: int):
            ans.append(ds[:])
            for i in range(ind, len(nums)):
                if i != ind and nums[i] == nums[i - 1]:
                    continue
                ds.append(nums[i])
                findSubsets(i + 1)
                ds.pop()
        nums.sort()
        findSubsets(0)
        return ans