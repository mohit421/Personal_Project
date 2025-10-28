'''

'''
# Next greater element 1
'''
TC:- O(N^2)
SC:- O(N)
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = []
        for x in nums1:
            # find index of x in nums2
            idx = nums2.index(x)
            # search to the right
            found = -1
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > x:
                    found = nums2[j]
                    break
            nge.append(found)
        return nge
    


# Solution 2 usign dict and monotonic stack
'''

Time Complexity:
O(n + len(nums1))
(linear in size of nums2 + size of nums1)

Space Complexity:
O(n)
(for the stack and mapping)
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        nge = {}
        for num in nums2:
            while st and st[-1] < num:
                nge[st.pop()] = num
            st.append(num)
        while st:
            nge[st.pop()] = -1
        
        return [nge[x] for x in nums1]
    

# Solution 3  neetcode ways
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n: i for i, n in enumerate(nums1)}   # FIXED
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break

        return res
    



# Solution 4  most effiecient usign stack by neetcode io

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        res = [-1]*len(nums1)

        st = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while st and curr > st[-1]:
                val = st.pop()
                idx = nums1Idx[val]
                res[idx] = curr
            
            if curr in nums1Idx:
                st.append(curr)
        
        return res