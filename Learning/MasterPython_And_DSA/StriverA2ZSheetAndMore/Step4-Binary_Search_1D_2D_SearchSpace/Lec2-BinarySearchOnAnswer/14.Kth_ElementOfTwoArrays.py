'''

'''

# Brute force


class Solution:

    def kthElement(self, a, b, k):
        ans = a + b
        ans.sort()

        l = len(ans)
        return ans[k-1]
    
# Brute force using Merge sort

#User function Template for python3


class Solution:

    def kthElement(self, nums1, nums2, k):
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
        return ans[k-1]


# optimized solution 

#User function Template for python3


class Solution:

    def kthElement(self, nums1, nums2, k):
        n1,n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.kthElement(nums2,nums1,k)
        lo,hi = max(0,k-n2), min(k,n1)
        left = k
        while lo<=hi:
            mid1 = (lo+hi)//2
            mid2 = left-mid1
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if mid1<n1:   r1 = nums1[mid1]
            if mid2<n2:   r2 = nums2[mid2]
            if mid1-1>=0:   l1 = nums1[mid1-1]
            if mid2-1>=0:   l2 = nums2[mid2-1]
            if l1<=r2 and l2<=r1:

                return max(l1,l2)

            elif l1>r2:
                hi = mid1-1
            else:
                lo = mid1+1
        return 0