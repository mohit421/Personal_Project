'''

'''

import bisect

class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        n = len(arr)
        low, high = 0, n - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                ans = mid         # update answer
                low = mid + 1     # keep looking to the right
            else:
                high = mid - 1
        return ans
        

# Using built in 

import bisect

class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        idx = bisect.bisect_right(arr, x)
        return idx - 1 if idx > 0 else -1