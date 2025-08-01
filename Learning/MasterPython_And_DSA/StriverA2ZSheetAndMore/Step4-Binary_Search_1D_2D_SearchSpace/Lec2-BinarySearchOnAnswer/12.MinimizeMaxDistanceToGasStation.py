'''
https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1
'''

# Brute force
'''
Complexity Analysis

Time Complexity: O(k*n) + O(n), n = size of the given array, k = no. of gas stations to be placed.
Reason: O(k*n) to insert k gas stations between the existing stations with maximum distance. Another O(n) for finding the answer i.e. the maximum distance.

Space Complexity: O(n-1) as we are using an array to keep track of placed gas stations.
'''
#User function Template for python3

class Solution:
    def findSmallestMaxDist(self, arr, k):
        # Code here
        n = len(arr)
        arrOfStation = [0]*(n-1)
        
        for gasSta in range(1,k+1):
            maxIdx,maxSec = -1,-1
            for i in range(n-1):
                diff = arr[i+1]-arr[i]
                diffLen = diff/(arrOfStation[i]+1)
                
                if diffLen > maxSec:
                    maxSec = diffLen
                    maxIdx = i
            
            arrOfStation[maxIdx] += 1
        
        
        maxAns = -1
        for i in range(n-1):
            diff = arr[i+1] - arr[i]
            diffLen = diff/(arrOfStation[i]+1)
            maxAns = max(maxAns,diffLen)
        return maxAns


#Solution 2  Better Solution using Heap               # 


# Solution 3 Optimised Solution iusing binary search

