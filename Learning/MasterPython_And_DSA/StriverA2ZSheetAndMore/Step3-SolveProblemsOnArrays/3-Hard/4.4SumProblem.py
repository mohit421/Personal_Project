'''

'''

# Solution 1 Brute force
'''
Time Complexity: O(N4), where N = size of the array.
Reason: Here, we are mainly using 4 nested loops. But we not considering the time complexity of sorting as we are just sorting 4 elements every time.

Space Complexity: O(2 * no. of the quadruplets) as we are using a set data structure and a list to store the quads.
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        st = set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        sm = nums[i] + nums[j] + nums[k] + nums[l]
                        if sm == target:
                            temp = [nums[i],nums[j],nums[k],nums[l]]
                            temp.sort()
                            st.add(tuple(temp))
        
        ans = [list(item) for item in st]
        return ans
    


# 1.1 brute force using list comprehension

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        st = set()
        [st.add(tuple(sorted([nums[i],nums[j],nums[k],nums[l]])))
            for i in range(n)
            for j in range(i+1,n)
            for k in range(j+1,n)
            for l in range(k+1,n)
            if nums[i] + nums[j] + nums[k] +nums[l] == target

        ]
        ans = [list(item) for item in st]
        return ans
    

# Using itertools combinations solution 1.3 brute force

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        st = set()
        for quad in combinations(nums,4):
            if sum(quad) == target:
                st.add(tuple(sorted(quad)))
        return [list(item) for item in st]
    


# Soluton 2 Better solution using hashing + loops
'''
Complexity Analysis

Time Complexity: O(N3*log(M)), where N = size of the array, M = no. of elements in the set.
Reason: Here, we are mainly using 3 nested loops, and inside the loops there are some operations on the set data structure which take log(M) time complexity.

Space Complexity: O(2 * no. of the quadruplets)+O(N)
Reason: we are using a set data structure and a list to store the quads. This results in the first term. And the second space is taken by the set data structure we are using to store the array elements. At most, the set can contain approximately all the array elements and so the space complexity is O(N).
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        st = set()
        for i in range(n):
            for j in range(i+1,n):
                hashset = set()
                for k in range(j+1,n):
                    fourth = target -(nums[i] + nums[j] + nums[k])
                    if fourth in hashset:
                        temp = [nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        st.add(tuple(temp))
                    hashset.add(nums[k])
                
        ans = list(st)
        return ans
                        
        
        ans = [list(item) for item in st]
        return ans
    

# Optimised Solution using two pointers

'''
Complexity Analysis

Time Complexity: O(N3), where N = size of the array.
Reason: Each of the pointers i and j, is running for approximately N times. And both the pointers k and l combined can run for approximately N times including the operation of skipping duplicates. So the total time complexity will be O(N3). 

Space Complexity: O(no. of quadruplets), This space is only used to store the answer. We are not using any extra space to solve this problem. So, from that perspective, space complexity can be written as O(1).

'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans  = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]: continue
            for j in range(i+1,n):
                if (j>i+1 and nums[j] == nums[j-1]): continue
                k = j+1
                l = n-1
                while k<l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum < target:
                        k += 1
                    elif sum> target:
                        l -= 1
                    else:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        ans.append(temp)
                        k += 1
                        l -= 1
                        while k<l and nums[k] == nums[k-1]:
                            k += 1
                        while k<l and nums[l] == nums[l+1]:
                            l -= 1
        return ans
