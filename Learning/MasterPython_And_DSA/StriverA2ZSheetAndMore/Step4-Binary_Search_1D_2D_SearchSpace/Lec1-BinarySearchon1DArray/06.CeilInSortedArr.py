'''
https://www.notion.so/DSA-Learning-Tracker-2025-by-Dev-Junk-22097d48b97a80b9a020d70e2426c288?pvs=47&qid=&origin=

'''


# Solution 
#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        # code here
        n = len(arr)
        low,high = 0,n-1
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]>=x:
                ans = mid
                high = mid-1
            else:
                low = mid + 1
        return ans