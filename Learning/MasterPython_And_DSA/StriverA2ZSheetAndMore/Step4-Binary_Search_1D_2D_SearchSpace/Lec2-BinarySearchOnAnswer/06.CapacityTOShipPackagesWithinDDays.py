'''

'''
# Solution 1 Brute Force

'''
Complexity Analysis

Time Complexity: O(N * (sum(weights[]) - max(weights[]) + 1)), where sum(weights[]) = summation of all the weights, max(weights[]) = maximum of all the weights, N = size of the weights array.
Reason: We are using a loop from max(weights[]) to sum(weights[]) to check all possible weights. Inside the loop, we are calling findDays() function for each weight. Now, inside the findDays() function, we are using a loop that runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''

class Solution:

    def findDays(self, weights: list[int], D:int):
        d = 1
        sm = 0
        n = len(weights)
        for i in range(n):
            if sm +weights[i] >D:
                d += 1
                sm = weights[i]
            else:
                sm += weights[i]
        return d

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mini = max(weights)
        maxi = sum(weights)
        for i in range(mini, maxi+1):
            if self.findDays(weights, i)<=days:
                return i
        return -1
            

# Solution  2 Using binary search
'''

'''

class Solution:

    def findDays(self, weights: list[int], D:int):
        d = 1
        sm = 0
        n = len(weights)
        for i in range(n):
            if sm +weights[i] >D:
                d += 1
                sm = weights[i]
            else:
                sm += weights[i]
        return d

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mini = max(weights)
        maxi = sum(weights)
        ans = 0
        while mini<=maxi:
            mid = (mini+maxi)//2
            if self.findDays(weights, mid)<=days:
                ans = mid
                maxi = mid-1
            else:
                mini = mid+1
        return ans
            

# Solution 3 Optimized one using binary search
'''

'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mini = max(weights)
        maxi = sum(weights)
        n = len(weights)
        lo, hi = mini,maxi
        while lo<hi:
            mid = (lo+hi)//2
            sm,d = 0,1
            for w in weights:
                if sm + w >mid:
                    d += 1
                    sm = 0
                sm += w
            if d>days:
                lo = mid+1
            else:
                hi = mid
        return lo
            