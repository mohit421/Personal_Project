'''

'''



# Soluition 1


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        lst = []
        arr = [1,2,3,4,5,6,7,8,9]
        def helper(ind,n):
            if n == 0 and k==len(lst):
                ans.append(lst[:])
                return
            for i in range(ind, len(arr)):
                if arr[i]>n:
                    break
                lst.append(arr[i])
                helper(i+1,n-arr[i])
                lst.pop()
        
        helper(0,n)
        return ans

# SOlution 2 avoid go in loop for more than number of 3 elememtn in list 

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        lst = []
        arr = [1,2,3,4,5,6,7,8,9]

        def helper(ind, remaining):
            if remaining == 0 and len(lst) == k:
                ans.append(lst[:])
                return
            if remaining < 0 or len(lst) > k:
                return
            for i in range(ind, len(arr)):
                if arr[i] > remaining:
                    break
                lst.append(arr[i])
                helper(i + 1, remaining - arr[i])  # <-- use i+1
                lst.pop()

        helper(0, n)
        return ans
