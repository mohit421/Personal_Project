''''
O((n + m) log(n + m))
'''


# Brute force

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine both arrays
        ans = nums1 + nums2
        ans.sort()

        l = len(ans)
        if l % 2 != 0:
            # Odd length, return the middle element
            return float(ans[l // 2])
        else:
            # Even length, return average of two middle elements
            mid1 = ans[l // 2 - 1]
            mid2 = ans[l // 2]
            return round((mid1 + mid2) / 2.0, 5)


# Another Brute force 
'''
Complexity Analysis

Time Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
Reason: We traverse through both arrays linearly.

Space Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
Reason: We are using an extra array of size (n1+n2) to solve this problem.
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine both arrays
        ans = []
        n1,n2 = len(nums1), len(nums2)
        i,j = 0,0
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1

        # we can do belowtwo while loop thing builtin func extends
        while i<n1:
            ans.append(nums1[i])
            i += 1
        while j<n2:
            ans.append(nums2[j])
            j += 1
         # copy the left-out elements:
        #  above two while loop code using built in 
        # ans.extend(nums1[i:])
        # ans.extend(nums2[j:])
        l = len(ans)
        if l % 2 != 0:
            # Odd length, return the middle element
            return float(ans[l // 2])
        else:
            # Even length, return average of two middle elements
            mid1 = ans[l // 2 - 1]
            mid2 = ans[l // 2]
            return round((mid1 + mid2) / 2.0, 5)


# Better solution 

# Focus on only two element if it is even  we don't need to merge all of them

'''
Complexity Analysis

Time Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
Reason: We traverse through both arrays linearly.

Space Complexity: O(1), as we are not using any extra space to solve this problem.
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine both arrays
        ans = []
        n1,n2 = len(nums1), len(nums2)
        i,j = 0,0
        el1, el2 = -1,-1
        cnt = 0
        n = (n1+n2)
        ind2 = n//2
        ind1 = ind2-1
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                if cnt == ind1 :
                    el1 = nums1[i]
                if cnt == ind2:
                    el2 = nums1[i]
                i += 1
                cnt += 1
            else:
                if cnt == ind1:
                    el1 = nums2[j]
                if cnt == ind2:
                    el2 = nums2[j]
                j += 1
                cnt += 1
            

        # we can do belowtwo while loop thing builtin func extends
        while i<n1:
            if cnt == ind1 :
                el1 = nums1[i]
            if cnt == ind2:
                el2 = nums1[i]
            i += 1
            cnt += 1
        while j<n2:
            if cnt == ind1:
                el1 = nums2[j]
            if cnt == ind2:
                el2 = nums2[j]
            j += 1
            cnt += 1
         # copy the left-out elements:
        #  above two while loop code using built in 
        # ans.extend(nums1[i:])
        # ans.extend(nums2[j:])
        if n%2==0:
            return (el1+el2)/2.0
        else:
            return el2


# Solution 3 Optimzed omne using binary serch
'''
Time Complexity: O(log(min(n1,n2))), where n1 and n2 are the sizes of two given arrays.
Reason: We are applying binary search on the range [0, min(n1, n2)].

Space Complexity: O(1) as no extra space is used.
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine both arrays
        n1,n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        lo,hi = 0,n1
        left = (n1+n2+1)//2
        n = n1+n2
        while lo<=hi:
            mid1 = (lo+hi)//2
            mid2 = left-mid1
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if mid1<n1:   r1 = nums1[mid1]
            if mid2<n2:   r2 = nums2[mid2]
            if mid1-1>=0:   l1 = nums1[mid1-1]
            if mid2-1>=0:   l2 = nums2[mid2-1]
            if l1<=r2 and l2<=r1:
                if n%2==1:
                    return max(l1,l2)
                return (float(max(l1,l2)) + float(min(r1,r2)))/2.0

            elif l1>r2:
                hi = mid1-1
            else:
                lo = mid1+1
        return 0
        
        