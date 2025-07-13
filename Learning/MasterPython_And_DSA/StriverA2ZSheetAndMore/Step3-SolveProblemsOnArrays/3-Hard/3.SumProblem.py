'''

'''

# Solution 1
'''
Complexity Analysis

Time Complexity: O(N3 * log(no. of unique triplets)), where N = size of the array.
Reason: Here, we are mainly using 3 nested loops. And inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

Space Complexity: O(2 * no. of the unique triplets) as we are using a set data structure and a list to store the triplets.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        st = set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        st.add(tuple(temp))
        ans = [list(item) for item in st]
                    
        return ans


# Brute force using list comprehension

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        st = set()
        [st.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        for i in range(n)
        for j in range(i+1,n)
        for k in range(j+1,n)
        if nums[i] + nums[j] + nums[k]==0
        ]
        return [list(item) for item in st]
                    
# Brute Force Using itertools.combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        st = set()
        for triplet in combinations(nums,3):
            if sum(triplet) == 0:
                st.add(tuple(sorted(triplet)))
        return [list(i) for i in st]
                    
# Brute Force  (Using a Custom Uniqueness Check)
# Without using set

class Solution:
    def is_unique(self, temp, res):
        for i in res:
            if sorted(temp) == sorted(i):
                return False
        return True
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] +nums[j] + nums[k] == 0:
                        temp = [nums[i],nums[j],nums[k]]
                        if self.is_unique(temp,res):
                            res.append(temp)
        return res

                    
'''

| Approach | Method                   | Uses Set? | Uses Sorting? | Readability       |
| -------- | ------------------------ | --------- | ------------- | ----------------- |
| 1        | `itertools.combinations` | ✅         | ✅             | ✅✅✅               |
| 2        | List comprehension       | ✅         | ✅             | ⚠️ Less readable  |
| 3        | Manual uniqueness check  | ❌         | ✅             | ✅ (for beginners) |

'''
                    
# Solution 2
# Better solution 
'''
Complexity Analysis

Time Complexity: O(N2 * log(no. of unique triplets)), where N = size of the array.
Reason: Here, we are mainly using 3 nested loops. And inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

Space Complexity: O(2 * no. of the unique triplets) + O(N) as we are using a set data structure and a list to store the triplets and extra O(N) for storing the array elements in another set.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        st = set()

        for i in range(n):
            hashset = set()
            for j in range(i+1,n):
                third = -(nums[i]+nums[j])
                if third in hashset:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    st.add(tuple(temp))
                hashset.add(nums[j])
        ans = list(st)

        return ans


                    

# Optimised Algo  Solution 3
'''
Complexity Analysis

Time Complexity: O(NlogN)+O(N2), where N = size of the array.
Reason: The pointer i, is running for approximately N times. And both the pointers j and k combined can run for approximately N times including the operation of skipping duplicates. So the total time complexity will be O(N2). 

Space Complexity: O(no. of quadruplets), This space is only used to store the answer. We are not using any extra space to solve this problem. So, from that perspective, space complexity can be written as O(1).
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if (i>0 and nums[i] == nums[i-1]):
                continue
            j = i+1
            k = n-1
            while j<k:
                sum = nums[i] +nums[j] + nums[k]
                if sum<0:
                    j += 1
                elif sum>0:
                    k -= 1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    while (j<k and nums[j] == nums[j-1]): j+=1
                    while (j<k and nums[k] == nums[k+1]): k -=1
        return ans
                


