''''

'''


# Solution 1 Brute force
'''
Complexity Analysis

Time Complexity: O((max(arr[])-min(arr[])+1) * N), where {max(arr[]) -> maximum element of the array, min(arr[]) -> minimum element of the array, N = size of the array}.
Reason: We are running a loop to check our answers that are in the range of [min(arr[]), max(arr[])]. For every possible answer, we will call the possible() function. Inside the possible() function, we are traversing the entire array, which results in O(N).

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''
class Solution:
    def miniNoDay(self, bloomDay: List[int],Day: int, m: int, k: int)->bool:
        n = len(bloomDay)
        cnt = 0
        noOfBou = 0
        for i in range(n):
            if bloomDay[i]<=Day:
                cnt += 1
            else:
                noOfBou += cnt//k
                cnt = 0
        noOfBou += cnt//k
        return noOfBou>=m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        posVal = m*k
        n = len(bloomDay)
        if posVal>n:
            return -1
        mini = min(bloomDay)
        maxi = max(bloomDay)
        for i in range(mini, maxi+1):
            if self.miniNoDay(bloomDay,i,m,k):
                return i
        return -1


# Solution 2

'''
Time Complexity: O(log(max(arr[])-min(arr[])+1) * N), where {max(arr[]) -> maximum element of the array, min(arr[]) -> minimum element of the array, N = size of the array}.
Reason: We are applying binary search on our answers that are in the range of [min(arr[]), max(arr[])]. For every possible answer ‘mid’, we will call the possible() function. Inside the possible() function, we are traversing the entire array, which results in O(N).

Space Complexity: O(1) as we are not using any extra space to solve this problem.

'''

class Solution:
    def miniNoDay(self, bloomDay: List[int],Day: int, m: int, k: int)->bool:
        n = len(bloomDay)
        cnt = 0
        noOfBou = 0
        for i in range(n):
            if bloomDay[i]<=Day:
                cnt += 1
            else:
                noOfBou += cnt//k
                cnt = 0
        noOfBou += cnt//k
        return noOfBou>=m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        posVal = m*k
        n = len(bloomDay)
        if posVal>n:
            return -1
        mini = min(bloomDay)
        maxi = max(bloomDay)

        while mini<=maxi:
            mid = (mini+maxi)//2
            if self.miniNoDay(bloomDay,mid,m,k):
                maxi = mid-1
            else:
                mini = mid+1
        return mini