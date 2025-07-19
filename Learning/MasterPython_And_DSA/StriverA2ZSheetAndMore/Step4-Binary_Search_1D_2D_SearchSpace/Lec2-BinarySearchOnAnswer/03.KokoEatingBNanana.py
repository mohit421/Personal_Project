'''

'''


# Brute force Sol 1
'''
Time Complexity: O(max(a[]) * N), where max(a[]) is the maximum element in the array and N = size of the array.
Reason: We are running nested loops. The outer loop runs for max(a[]) times in the worst case and the inner loop runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''
class Solution:
    def findMax(self,piles):
        maxi = float(-inf)
        n = len(piles)
        for i in range(n):
            maxi = max(maxi,piles[i])
        return maxi
    
    def calctTotalHour(self,piles, hours):
        totH = 0
        n = len(piles)
        for i in range(n):
            totH += math.ceil(piles[i]/hours)
        return totH
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = self.findMax(piles)
        for i in range(1,maxi+1):
            totalHour = self.calctTotalHour(piles,i)
            if totalHour<=h:
                return i
        return maxi
    

# Optimised solu usinfg binary search

'''
Time Complexity: O(N * log(max(a[]))), where max(a[]) is the maximum element in the array and N = size of the array.
Reason: We are applying Binary search for the range [1, max(a[])], and for every value of ‘mid’, we are traversing the entire array inside the function named calculateTotalHours().

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''

class Solution:
    def findMax(self,piles):
        maxi = float(-inf)
        n = len(piles)
        for i in range(n):
            maxi = max(maxi,piles[i])
        return maxi
    
    def calcTotalHour(self,piles, hours):
        totH = 0
        n = len(piles)
        for i in range(n):
            totH += math.ceil(piles[i]/hours)
        return totH
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo,hi = 1, self.findMax(piles)
        ans = sys.maxsize
        while lo<=hi:
            mid = (lo+hi)//2
            totH = self.calcTotalHour(piles, mid)
            if totH<=h:
                ans = min(ans, mid)
                hi = mid-1
            else:
                lo = mid+1
        # return ans
        return lo



# 