'''


'''

# Soluytion 1 Brute Force
'''
Time Complexity: O(N^2) { Since there are nested loops being used, at the worst case n^2 time would be consumed }.

Space Complexity: O(N) { There is no extra space being used in this approach. But, a O(N) of space for ans array will be used in the worst case }.

'''
class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        res = []
        
        for i in range(n):
            leader = True
            for j in range(i+1,n):
                if arr[i]<arr[j]:
                    leader = False
            if leader:
                res.append(arr[i])
        return res





# Solution 2 

'''
Time Complexity: O(N) { Since the array is traversed single time back to front, it will consume O(N) of time where N = size of the array }.

Space Complexity: O(N) { There is no extra space being used in this approach. But, a O(N) of space for ans array will be used in the worst case }.
'''

class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        res = []
        maxi = arr[-1]
        res.append(maxi)
        for i in range(n-2,-1,-1):
            if arr[i] >= maxi:
                maxi = arr[i]
                res.append(maxi)
        return res[::-1]