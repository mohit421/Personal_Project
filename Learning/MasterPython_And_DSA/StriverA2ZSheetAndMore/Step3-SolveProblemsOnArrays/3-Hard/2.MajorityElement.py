'''

'''

# SOlution 1 Brute Force Approach
'''

First I am confuse why bhaiya is using ls.size ==2 then I check it manually by taking test cases then i come to know the reason behind it ..
nums= [1,1,1,2,2,2,3,3,3] or nums=[1,1,1,1,2,2,2,2,3,3,3,3]





Complexity Analysis

Time Complexity: O(N2), where N = size of the given array.
Reason: For every element of the array the inner loop runs for N times. And there are N elements in the array. So, the total time complexity is O(N2).

Space Complexity: O(1) as we are using a list that stores a maximum of 2 elements. The space used is so small that it can be considered constant.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        sz = n//3
        ls = []
        for i in range(n):
            if len(ls) == 0 or ls[0] != nums[i]:
                cnt = 0
                for j in range(n):
                    if nums[j] == nums[i]:
                        cnt += 1
                if cnt > sz:
                    ls.append(nums[i])
            if len(ls) == 2:
                break
        return ls


# Solution 2 Better Approach Used Hashing

'''
Complexity Analysis

Time Complexity: O(N) + O(N), where N = size of the given array.
Reason: The first O(N) is to calculate the counts and find the expected majority elements. The second one is to check if the calculated elements are the majority ones or not.

Space Complexity: O(1) as we are only using a list that stores a maximum of 2 elements. The space used is so small that it can be considered constant.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        ans = []
        for num,count in counter.items():
            if count >n//3:
                ans.append(num)
        return ans
    

# Extended Boyer-Moore Majority Voting 

# SSolution 3 Optimise solution \

'''
Complexity Analysis

Time Complexity: O(N) + O(N), where N = size of the given array.
Reason: The first O(N) is to calculate the counts and find the expected majority elements. The second one is to check if the calculated elements are the majority ones or not.

Space Complexity: O(1) as we are only using a list that stores a maximum of 2 elements. The space used is so small that it can be considered constant.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n  = len(nums)
        cnt1, cnt2 = 0, 0 # counts
        el1, el2 = float('-inf'), float('-inf')
        
        for i in range(n):
            if cnt1 == 0 and el2 != nums[i]:
                cnt1 = 1
                el1 = nums[i]
            elif cnt2 == 0 and el1 != nums[i]:
                cnt2 = 1
                el2 = nums[i]
            elif nums[i] == el1:
                cnt1 += 1
            elif nums[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ls = []
        cnt1 ,cnt2 = 0,0
        for i in range(n):
            if el1 == nums[i]:
                cnt1 += 1
            elif el2==nums[i]:
                cnt2 += 1
    
        mini = n//3
        if cnt1 > mini:
            ls.append(el1)
        if cnt2 > mini:
            ls.append(el2)
        return ls