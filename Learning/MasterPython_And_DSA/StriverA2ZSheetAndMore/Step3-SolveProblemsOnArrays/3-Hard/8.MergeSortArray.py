'''
Problem youtube solution link:- vhttps://www.youtube.com/watch?v=P1Ic85RarKY&ab_channel=NeetCode


'''

# Solution 1 
'''
TC:- O(N) + O((M+N)Log(M+N))
SC:- (1)
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()
        return nums1
    

# Solution 2 Brute force

'''
Time Complexity: O(n+m) + O(n+m), where n and m are the sizes of the given arrays.
Reason: O(n+m) is for copying the elements from arr1[] and arr2[] to arr3[]. And another O(n+m) is for filling back the two given arrays from arr3[].

Space Complexity: O(n+m) as we use an extra array of size n+m.
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = 0,0,0
        res = [0]*(m+n)
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                res[k] = nums1[i]
                i += 1
            else:
                res[k] = nums2[j]
                j += 1
            k += 1
        
        while i<m:
            res[k] = nums1[i]
            i,k = i+1, k+1
        while j<n:
            res[k] = nums2[j]
            j,k = j+1,k+1
        
        for k in range(n+m):
            nums1[k] = res[k]

# Soluiton 3 optimised solution 

# Wihout using extra spaces aray inplace
'''

'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n -1

        while n > 0 and m> 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        while n>0:
            nums1[last] = nums2[n-1]
            n, last  = n-1, last-1
        

