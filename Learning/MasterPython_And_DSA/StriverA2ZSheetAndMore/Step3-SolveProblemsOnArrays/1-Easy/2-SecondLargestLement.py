'''

'''

# Using sort function
class Solution:
    def getSecondLargest(self, arr):
        # Code Here]
        mx = max(arr)
        arr.sort()
        for i in range(len(arr)-1,-1,-1):
            if mx!= arr[i]:
                return arr[i]
        return -1
    

# Better solution
'''
Complexity Analysis

Time Complexity: O(N), We do two linear traversals in our array

Space Complexity: O(1)
'''
class Solution:
    def getSecondLargest(self, arr):
        # Code Here]
        n = len(arr)
        if n==0 or n==1:
            return -1
        large = -1
        second_large = -1
        for i in range(n):
            large = max(large,arr[i])
        for i in range(n):
            if arr[i]> second_large and arr[i] != large:
                second_large = arr[i]
                
        return second_large
                

# Optimised solution

'''
Complexity Analysis

Time Complexity: O(N), We do two linear traversals in our array

Space Complexity: O(1)
'''

def secondLargest(arr,n):
    if n<2:
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if arr[i]> large:
            second_large = large 
            large = arr[i]
        elif arr[i]> second_large and arr[i] != large:
            second_large = arr[i]
    
    return second_large



# Optimized solution 
'''
Complexity Analysis

Time Complexity: O(N), Single-pass solution

Space Complexity: O(1)
'''
class Solution:
    def getSecondLargest(self, arr):
        # Code Here]
        n = len(arr)
        if n<2:
            return -1
        large = -1
        second_large = -1
        for i in range(n):
            if arr[i]> large:
                second_large = large 
                large = arr[i]
            elif arr[i]> second_large and arr[i] != large:
                second_large = arr[i]
        
        return second_large
