'''

'''

# SOlution 1 Brute Force
'''

Time Complexity: O(N+N/2) { O(N) for traversing the array once for segregating positives and negatives and another O(N/2) for adding those elements alternatively to the array, where N = size of the array A}.

Space Complexity:  O(N/2 + N/2) = O(N) { N/2 space required for each of the positive and negative element arrays, where N = size of the array A}.
'''
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        pos = []
        neg = []
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        for i in range(len(pos)):
            nums[2*i] = pos[i]
        for i in range(len(neg)):
            nums[2*i+1] = neg[i]
        return nums
    

# Solution 2 Slightly better than above one
'''
Time Complexity: O(N) { O(N) for traversing the array once and substituting positives and negatives simultaneously using pointers, where N = size of the array A}.

Space Complexity:  O(N) { Extra Space used to store the rearranged elements separately in an array, where N = size of array A}.
'''
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0]*(len(nums))
        posIdx = 0
        negIdx = 1
        for i in nums:
            if i<0:
                ans[negIdx] = i
                negIdx += 2
            else:
                ans[posIdx] = i
                posIdx += 2
        return ans
    

# Vareity 2 problem 
'''
Problem Link :- https://www.naukri.com/code360/problems/alternate-numbers_6783445?isSignin=true


Codestudio Problem :- Alternate Numbers

if something left just add them to the last 
'''

# Brute force
'''
Time Complexity: O(2*N) { The worst case complexity is O(2*N) which is a combination of O(N) of traversing the array to segregate into neg and pos array and O(N) for adding the elements alternatively to the main array}.

Explanation: The second O(N) is a combination of O(min(pos, neg)) + O(leftover elements). There can be two cases: when only positive or only negative elements are present, O(min(pos, neg)) + O(leftover) = O(0) + O(N), and when equal no. of positive and negative elements are present, O(min(pos, neg)) + O(leftover) = O(N/2) + O(0). So, from these two cases, we can say the worst-case time complexity is O(N) for the second part, and by adding the first part we get the total complexity of O(2*N).

Space Complexity:  O(N/2 + N/2) = O(N) { N/2 space required for each of the positive and negative element arrays, where N = size of the array A}.
'''
from typing import List

def alternateNumbers(a: List[int]) -> List[int]:
    pos = []
    neg = []
    
    # Separate positive and negative numbers
    for i in a:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    
    res = []
    i = j = 0
    # Alternate between pos and neg
    while i < len(pos) and j < len(neg):
        res.append(pos[i])
        res.append(neg[j])
        i += 1
        j += 1
    
    # Add remaining elements if any
    while i < len(pos):
        res.append(pos[i])
        i += 1
    
    while j < len(neg):
        res.append(neg[j])
        j += 1
    
    return res





