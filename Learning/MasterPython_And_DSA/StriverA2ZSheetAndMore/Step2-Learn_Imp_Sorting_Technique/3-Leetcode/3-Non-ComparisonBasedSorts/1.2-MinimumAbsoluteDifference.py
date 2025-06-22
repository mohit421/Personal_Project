# Solution 1

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort();
        distLst = []
        absDiff = arr[1]- arr[0]
        for i in range(len(arr)-1):
            mabsDiff = abs(arr[i]-arr[i+1])
            if absDiff>mabsDiff:
                absDiff = mabsDiff
                # distLst.clear()
                distLst = [[arr[i],arr[i+1]]]
            elif absDiff == mabsDiff:
                distLst.append([arr[i],arr[i+1]])
        return distLst
                


# Solution 2
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort();
        distLst = []
        absDiff = arr[1]- arr[0]
        for i in range(len(arr)-1):
            mabsDiff = abs(arr[i]-arr[i+1])
            if absDiff>mabsDiff:
                absDiff = mabsDiff
                distLst.clear()
                distLst.append([[arr[i],arr[i+1]]])
            elif absDiff == mabsDiff:
                distLst.append([arr[i],arr[i+1]])
        return distLst
                