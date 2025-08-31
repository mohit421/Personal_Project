'''

'''

# Solution


'''

'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        lst = []
        candidates.sort()

        def findComb2(ind: int, target:int):
            if target ==0 :
                ans.append(lst[:])
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i] == candidates[i-1]:
                    continue
    
                if candidates[i]> target:
                    break
            
                lst.append(candidates[i])
                findComb2(i+1, target-candidates[i])
                lst.pop()

        findComb2(0, target)
        return ans
    


# sSolution 2
'''
TC: - O(2^n*k)
SC:- K*X
where x is no of  combination
'''
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()   # sort to handle duplicates
        lst = []

        def backtrack(start: int, target: int):
            if target == 0:
                ans.append(lst[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                lst.append(candidates[i])
                # move to next index, because each element can be used at most once
                backtrack(i+1, target - candidates[i])
                lst.pop()

        backtrack(0, target)
        return ans
