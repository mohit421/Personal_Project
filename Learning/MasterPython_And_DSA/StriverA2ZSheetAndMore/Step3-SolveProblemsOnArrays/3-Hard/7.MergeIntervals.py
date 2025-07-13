'''

'''


# Solution 1


# Brute force
'''
Time Complexity: O(N*logN) + O(2*N), where N = the size of the given array.
Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are using 2 loops i and j. But while using loop i, we skip all the intervals that are merged with loop j. So, we can conclude that every interval is roughly visited twice(roughly, once for checking or skipping and once for merging). So, the time complexity will be 2*N instead of N2.

Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array, we are not using any extra space.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        ans= []
        intervals.sort()
        for i in range(n):
            s,e = intervals[i][0], intervals[i][1]
            if ans and  e<=ans[-1][1]:
                continue
            for j in range(i+1,n):
                if intervals[j][0] <= e:
                    e = max(e, intervals[j][1])
                else:
                    break
            ans.append([s,e])
        return ans
    

# Optimised approaches solutions 2 
'''
Complexity Analysis

Time Complexity: O(N*logN) + O(N), where N = the size of the given array.
Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are just using a single loop that runs for N times. So, the time complexity will be O(N).

Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array, we are not using any extra space.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        ans= []
        intervals.sort()
        for i in range(n):
            if not ans or  intervals[i][0]>ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])

        return ans
    
# Solution 3

'''
Complexity
Time complexity: O(nlogn) (for sorting)
Space complexity: O(n) (for storing merged intervals)
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        ans= []
        intervals.sort()
        prev = intervals[0]
        for i in range(1,n):
            if intervals[i][0]>prev[1]:
                prev[1] = max(prev[1],intervals[i][1])
            else:
                ans.append(prev)
                prev = intervals[i]
        ans.append(prev)
        return ans