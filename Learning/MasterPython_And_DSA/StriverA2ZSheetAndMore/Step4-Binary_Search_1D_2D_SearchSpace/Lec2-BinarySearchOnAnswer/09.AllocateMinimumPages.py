'''

'''

# Solution 1 Brute Force 
'''
Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are using a loop from max(arr[]) to sum(arr[]) to check all possible numbers of pages. Inside the loop, we are calling the countStudents() function for each number. Now, inside the countStudents() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
'''
class Solution:
    
    
    def possibleStudent(self, arr, pages):
        n = len(arr)
        stu = 1
        pagesSt = 0
        for i in range(n):
            if pagesSt + arr[i] <=pages:
                pagesSt += arr[i]
            else:
                stu += 1
                pagesSt = arr[i]
        return stu
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        n = len(arr)
        if k>n:
            return -1
        lo,hi = max(arr), sum(arr)
        for i in range(lo,hi+1):
            if self.possibleStudent(arr,i)==k:
                return i
        return lo
                
# Solution 2 Optimised One

'''
Complexity Analysis

Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countStudents() function for the value of ‘mid’. Now, inside the countStudents() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.

'''

class Solution:
    
    
    def possibleStudent(self, arr, pages):
        n = len(arr)
        stu = 1
        pagesSt = 0
        for i in range(n):
            if pagesSt + arr[i] <=pages:
                pagesSt += arr[i]
            else:
                stu += 1
                pagesSt = arr[i]
        return stu
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        n = len(arr)
        if k>n:
            return -1
        lo,hi = max(arr), sum(arr)
        while lo<=hi:
            mid = (lo+hi)//2
            students = self.possibleStudent(arr,mid)
            if students>k:
                lo = mid+1
            else:
                hi = mid-1
        return lo
                
