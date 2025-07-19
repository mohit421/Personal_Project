'''

'''
# Brute force 


class Solution:
    def findKRotation(self, arr):
        # code here
        min_val = arr[0]
        min_index = 0

        for i in range(1, len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
                min_index = i

        return min_index
            


            
# Solution Optimised one

class Solution:
    def findKRotation(self, arr):
        # code here
        n=len(arr)
        lo,hi = 0,n-1

        while lo<=hi:
            if arr[lo]<=arr[hi]:
                return lo
            
            mid = (lo+hi)//2
            next_idx = (mid+1)%n
            prev_idx = (mid-1+n)%n
            
            if arr[mid]<=arr[next_idx] and arr[mid]<=arr[prev_idx]:
                return mid
                
            if arr[mid]>=arr[lo]:
                lo = mid+1
            else:
                hi = mid-1
            