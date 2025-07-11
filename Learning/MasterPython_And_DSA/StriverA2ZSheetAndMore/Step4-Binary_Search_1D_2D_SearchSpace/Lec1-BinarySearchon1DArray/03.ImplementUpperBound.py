'''

https://www.notion.so/DSA-Learning-Tracker-2025-by-Dev-Junk-22097d48b97a80b9a020d70e2426c288?pvs=47&qid=&origin=
'''

'''
| C++ STL       | Python (`bisect` module)      | Description                                                  |
| ------------- | ----------------------------- | ------------------------------------------------------------ |
| `lower_bound` | `bisect.bisect_left(arr, x)`  | First position where `x` can be inserted to keep order (≥ x) |
| `upper_bound` | `bisect.bisect_right(arr, x)` | First position where inserting `x` still keeps elements < x  |

upper = bisect.bisect_right(arr, x) 
'''

# Solution usign built in 
class Solution:
    def upperBound(self, arr, target):
        #code here
        return bisect.bisect_right(arr, target) 
    

# Siolution 2 Iterative way
'''
Complexity Analysis

Time Complexity: O(logN), where N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''
class Solution:
    def upperBound(self, arr, target):
        #code here
        n = len(arr)
        low,high = 0,n-1
        ans = n
        while low<=high:
            if low>high:
                return ans
            mid = (low + high)//2
            if arr[mid]>target:
                high = mid-1
                ans = mid
            else:
                low = mid+1
        return ans
    


# Solution 3 recursive way
class Solution:
    
    def lowerBound(self, arr, x):
        #code here
        def binarySearch(low,high,ans):
            if low>high:
                return ans
            mid = (low+high)//2
            if arr[mid]>x:
                return binarySearch(low,mid-1,mid)
            else:
                return binarySearch(mid+1,high, ans)
        
        return binarySearch(0,len(arr)-1,len(arr))