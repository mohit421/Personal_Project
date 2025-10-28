'''

'''


# Brute force


class Solution:
    def count_NGE(self, arr, indices):
        # Code here
        n = len(arr)
        q = len(indices)
        ans = []
        for i in indices:
            cnt = 0
            for j in range(i+1,n):
                if arr[j]>arr[i]:
                    cnt += 1
            
            ans.append(cnt)
        
        return ans
        

#  Optimal Approach

