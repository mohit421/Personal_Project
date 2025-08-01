'''
LinK:- https://www.notion.so/DSA-Learning-Tracker-2025-by-Dev-Junk-22097d48b97a80b9a020d70e2426c288?pvs=47&qid=&origin=
'''

''''
For more details go to :- https://takeuforward.org/data-structure/binary-search-explained/
Note:

Binary search is only applicable in a sorted search space. The sorted search space does not necessarily have to be a sorted array. It can be anything but the search space must be sorted.
In binary search, we generally divide the search space into two equal halves and then try to locate which half contains the target. According to that, we shrink the search space size.
'''

# Soluton 1 Iterative ways
'''
Time Complexity:
In the algorithm, in every step, we are basically dividing the search space into 2 equal halves. This is actually equivalent to dividing the size of the array by 2, every time. After a certain number of divisions, the size will reduce to such an extent that we will not be able to divide that anymore and the process will stop. The number of total divisions will be equal to the time complexity.

Let’s derive the number of divisions mathematically,

If a number n can be divided by 2 for x times:
	2^x = n
Therefore, x = logn (base is 2)
So the overall time complexity is O(logN), where N = size of the given array.
'''

#include <bits/stdc++.h>
using namespace std;

int binarySearch(vector<int>& nums, int target) {
    int n = nums.size(); //size of the array
    int low = 0, high = n - 1;

    // Perform the steps:
    while (low <= high) {
        int mid = (low + high) / 2;
        if (nums[mid] == target) return mid;
        else if (target > nums[mid]) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}


# Solution 2 Recursive appraoch
'''
Complexity Analysis

Time Complexity:
In the algorithm, in every step, we are basically dividing the search space into 2 equal halves. This is actually equivalent to dividing the size of the array by 2, every time. After a certain number of divisions, the size will reduce to such an extent that we will not be able to divide that anymore and the process will stop. The number of total divisions will be equal to the time complexity.

Let’s derive the number of divisions mathematically,

If a number n can be divided by 2 for x times:
	2^x = n
Therefore, x = logn (base is 2)
So the overall time complexity is O(logN), where N = size of the given array.
'''
class Solution:
    def helper(self, nums, low, high, target):
        if low>high:
            return -1
        else:
            mid = (low+high)//2
            if nums[mid] == target:
                return  mid
            elif nums[mid]>target:
                return self.helper(nums,low,mid-1,target)
            else:
                return self.helper(nums,mid+1,high,target)

        
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums)-1,target)
    
    

'''
In case of c++:- OVERFLOW CASE
if we are taking array length of size maximum of INT_MAX 
let say if your reached to INT_MAX:- that's may be possible case
then 2*IN_MAX will Overflow

Two Solution of this is:-
1. take long long 
2. mid = low + (high-low)//2 - alenative way to find mid that's math
'''