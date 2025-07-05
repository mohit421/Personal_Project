'''

'''

# Solution 1 Brute force

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