'''

'''
# Solution 1


import bisect
class Solution:
    def countFreq(self, arr, target):
        #code here
        lo = bisect.bisect_left(arr,target)
        hi = bisect.bisect_right(arr,target)
        if lo == len(arr) or arr[lo] != target:
            return 0
        return hi-lo
            
        