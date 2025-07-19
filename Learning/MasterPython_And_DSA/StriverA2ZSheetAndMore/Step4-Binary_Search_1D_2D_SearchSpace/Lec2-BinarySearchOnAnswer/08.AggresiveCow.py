'''

'''

# Solution 1 Brute force
'''
Time Complexity: O(NlogN) + O(N *(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.
Reason: O(NlogN) for sorting the array. We are using a loop from 1 to max(stalls[])-min(stalls[]) to check all possible distances. Inside the loop, we are calling canWePlace() function for each distance. Now, inside the canWePlace() function, we are using a loop that runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.

'''

class Solution:
    def possibleDist(self,stalls,dist,cow):
        n = len(stalls)
        last = stalls[0]
        cntCow = 1
        for i in range(1,n):
            if stalls[i] - last >=dist:
                cntCow +=1 
                last = stalls[i]
            if cntCow>=cow:
                return True
        return False
    def aggressiveCows(self, stalls, k):
        # your code here
        stalls.sort()
        n  = len(stalls)
        d = stalls[n-1] - stalls[0]
        for i in range(1,d+1):
            if not self.possibleDist(stalls,i,k):
                return i-1
        return d
    

# Solution 2 Using binary search on answer

'''
Complexity Analysis

Time Complexity: O(NlogN) + O(N * log(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.
Reason: O(NlogN) for sorting the array. We are applying binary search on [1, max(stalls[])-min(stalls[])]. Inside the loop, we are calling canWePlace() function for each distance, ‘mid’. Now, inside the canWePlace() function, we are using a loop that runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''

class Solution:
    def possibleDist(self,stalls,dist,cow):
        n = len(stalls)
        last = stalls[0]
        cntCow = 1
        for i in range(1,n):
            if stalls[i] - last >=dist:
                cntCow +=1 
                last = stalls[i]
            if cntCow>=cow:
                return True
        return False
    def aggressiveCows(self, stalls, k):
        # your code here
        stalls.sort()
        n  = len(stalls)
        d = stalls[n-1] - stalls[0]
        lo,hi = 1,d
        while lo<=hi:
            mid = (lo+hi)//2
            if self.possibleDist(stalls,mid,k):
                lo = mid+1
            else:
                hi = mid -1
        return hi