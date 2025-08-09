'''
1781. Sum of Beauty of All Substrings
'''



'''
Complexity
Time complexity: O(n 
2
 )
Both the outer and inner loop runs n times.
The max() and min() are performed over at most 26 elements (a–z), so they're constant time.
Space complexity: O(1)
The frequency counter holds at most 26 characters (lowercase English letters), so space is constant.
'''

# Solution 1
class Solution:
    def beautySum(self, s: str) -> int:
        tot_b = 0
        for i in range(len(s)):
            freq = Counter()
            for j in range(i, len(s)):
                freq[s[j]] += 1
                tot_b += max(freq.values()) - min(freq.values())
        return tot_b
    

# Solution 2

class Solution:
    def beautySum(self, s: str) -> int:
        tot_b = 0
        for i in range(len(s)):
            freq = [0]*26
            for j in range(i, len(s)):
                freq[ord(s[j])-97] += 1
                tot_b += max(freq) - min(x for x in freq if x)
        return tot_b
    

# Detailed optimised sol

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        tot_b = 0
        for i in range(n):
            freq = [0]*26
            max_freq = 0
            for j in range(i,n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1
                max_freq = max(freq[idx], max_freq)
                min_freq = float('inf')
                for f in freq:
                    if f>0:
                        min_freq = min(min_freq,f)
                tot_b += max_freq - min_freq
        return tot_b
                