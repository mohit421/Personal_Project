'''

'''

#  SOlution 1
'''
Total Time Complexity:
👉 O(n log n + m)
Where:

n = number of strings

m = length of the shortest string (in the first/last position after sorting)


Total Space Complexity:
👉 O(1) (excluding the input and result)
or
👉 O(m) if you count the result string (which is usually acceptable).
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort()
        n = len(strs)
        f,l = strs[0], strs[n-1]
        for i in range(min(len(f), len(l))):
            if f[i] != l[i]:
                return ans
            ans += f[i]
        return ans
    

# Another ways  
'''
TC:- O(M*N)
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans