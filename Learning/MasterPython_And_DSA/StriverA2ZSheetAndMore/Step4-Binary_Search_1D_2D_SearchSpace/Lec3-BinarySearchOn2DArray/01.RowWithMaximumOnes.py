'''

'''


# Brute force

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        cnt_max = 0
        index = 0
        n,m = len(mat), len(mat[0])
        # traverse the matrix:
        for i in range(n):
            cnt_ones = sum(mat[i])
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
        return [index, cnt_max]
    

''''
In sorted column case we can applly binary serach like below code
'''


def lowerBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    return ans

def rowWithMax1s(matrix, n, m):
    cnt_max = 0
    index = -1

    # traverse the rows:
    for i in range(n):
        # get the number of 1's:
        cnt_ones = m - lowerBound(matrix[i], m, 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
n = 3
m = 3
print("The row with maximum no. of 1's is:", rowWithMax1s(matrix, n, m))