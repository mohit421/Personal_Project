'''

'''
# Brute force approach

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            hash = [0]*3
            for j in range(i,len(s)):
                hash[ord(s[j]) - ord('a')] = 1
                if hash[0] + hash[1] + hash[2] == 3:
                    cnt += 1
        return cnt
    

# Solution Optimised one using hashmap

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l,res = 0,0
        count = [0]*3
        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] += 1
            while count[0] and count[1] and count[2]:
                res += (len(s) - r)
                count[ord(s[l]) - ord('a')]-= 1
                l += 1
        return res
    



# Solution 2 using array to little bit optimised above one

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l,res = 0,0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            while len(count) == 3:
                res += (len(s) - r)
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l += 1
        return res
    

# Most optimised one

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = 0
        lastseen = [-1,-1,-1]
        for i in range(len(s)):
            lastseen[ord(s[i]) - ord('a')] = i
            if -1 not in lastseen:
                cnt += min(lastseen) + 1
        return cnt