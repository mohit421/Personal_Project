'''

'''

# Solution 1 Brute force
'''
TC:- O(N^2)
SC:- O(1)
'''
class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        n = len(arr)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                if a[i] > a[j]:
                    cnt += 1
        return cnt
    


# SOlution 2 Optimised solution

# Usinf Merge Sort concept
'''
Time Complexity: O(N*logN), where N = size of the given array.
Reason: We are not changing the merge sort algorithm except by adding a variable to it. So, the time complexity is as same as the merge sort.

Space Complexity: O(N), as in the merge sort We use a temporary array to store elements in sorted order.
'''


class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def __init__(self):
        self.cnt = 0  # initialize inversion counter
    def merge(self,arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1
    
        # Merge the two halves into temp
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            # right is smaller
            else:
                temp.append(arr[right])
                self.cnt += (mid - left +1)
                right += 1
    
        # Append remaining elements from left half (if any)
        while left <= mid:
            temp.append(arr[left])
            left += 1
    
        # Append remaining elements from right half (if any)
        while right <= high:
            temp.append(arr[right])
            right += 1
    
        # Copy sorted temp back into original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
    
    def mergeSort(self,arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)


    def inversionCount(self, arr):
        # Your Code Here
        n = len(arr)
        self.mergeSort(arr,0,n-1)
        return self.cnt
        
        
        
        
        
        