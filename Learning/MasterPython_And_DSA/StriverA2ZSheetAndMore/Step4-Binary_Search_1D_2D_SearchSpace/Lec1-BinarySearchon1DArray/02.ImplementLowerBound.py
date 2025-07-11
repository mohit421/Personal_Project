'''
https://www.notion.so/DSA-Learning-Tracker-2025-by-Dev-Junk-22097d48b97a80b9a020d70e2426c288?pvs=47&qid=&origin=



Python has built-in modules that provide similar functionality to C++'s lower_bound and upper_bound from the STL.

✅ Equivalent in Python: bisect module
The bisect module in Python provides bisect_left and bisect_right, which are equivalent to:

lower_bound → bisect.bisect_left

upper_bound → bisect.bisect_right


'''
'''
import bisect

arr = [1, 3, 3, 5, 7, 9]

x = 3

lower = bisect.bisect_left(arr, x)   # First index where arr[i] >= x
upper = bisect.bisect_right(arr, x)  # First index where arr[i] > x

print("Lower bound:", lower)  # Output: 1
print("Upper bound:", upper)  # Output: 3

'''

# Solution Brute force
'''
Complexity Analysis

Time Complexity: O(N), where N = size of the given array.
Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''
class Solution:
    
    def lowerBound(self, arr, x):
        #code here
        n = len(arr)
        for i in range(n):
            if arr[i] >= x:
                #lower bound found
                return i
        return n

# Solution 1Iterative solution 
'''
Complexity Analysis

Time Complexity: O(logN), where N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are using no extra space.
'''
class Solution:
    def lowerBound(self, arr, x):
        #code here
        n = len(arr)
        low,high = 0, n-1
        ans = n
        while low<=high:
            
            mid = (low+high)//2
            if arr[mid] >= x:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
            

# Solution 2 Recursive solution

'''
Time Complexity:
In the algorithm, in every step, we are basically dividing the search space into 2 equal halves. This is actually equivalent to dividing the size of the array by 2, every time. After a certain number of divisions, the size will reduce to such an extent that we will not be able to divide that anymore and the process will stop. The number of total divisions will be equal to the time complexity.

Let’s derive the number of divisions mathematically,

If a number n can be divided by 2 for x times:
	2^x = n
Therefore, x = logn (base is 2)
So the overall time complexity is O(logN), where N = size of the given array.
'''
class Solution:
    
    def lowerBound(self, arr, x):
        #code here
        def binarySearch(low,high,ans):
            if low>high:
                return ans
            mid = (low+high)//2
            if arr[mid]>=x:
                return binarySearch(low,mid-1,mid)
            else:
                return binarySearch(mid+1,high, ans)
        
        return binarySearch(0,len(arr)-1,len(arr))