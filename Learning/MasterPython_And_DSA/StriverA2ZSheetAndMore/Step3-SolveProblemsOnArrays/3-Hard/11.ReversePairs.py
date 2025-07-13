'''

'''


# Solution 1 Brute force

'''
Complexity Analysis

Time Complexity: O(N2), where N = size of the given array.
Reason: We are using nested loops here and those two loops roughly run for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i]> 2*nums[j]:
                    cnt += 1
        return cnt


# Solution 2
# Optimized solution using merge sort concept
'''
Complexity Analysis

Time Complexity: O(2N*logN), where N = size of the given array.
Reason: Inside the mergeSort() we call merge() and countPairs() except mergeSort() itself. Now, inside the function countPairs(), though we are running a nested loop, we are actually iterating the left half once and the right half once in total. That is why, the time complexity is O(N). And the merge() function also takes O(N). The mergeSort() takes O(logN) time complexity. Therefore, the overall time complexity will be O(logN * (N+N)) = O(2N*logN).

Space Complexity: O(N), as in the merge sort We use a temporary array to store elements in sorted order.
'''
class Solution:

    def __init__(self):
        self.cnt = 0
    def merge(self,arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        # Merge the two halves into temp
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
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

    def countPairs(self, arr, low, mid, high):
        right = mid + 1
        for i in range(low, mid+1):
            while right <=high and arr[i]>2*arr[right]:
                right += 1

            self.cnt += (right - (mid+1))
            
    def mergeSort(self,arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.countPairs(arr,low,mid,high)
        self.merge(arr, low, mid, high)


    
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        self.mergeSort(nums, 0, len(nums)-1)
        return self.cnt