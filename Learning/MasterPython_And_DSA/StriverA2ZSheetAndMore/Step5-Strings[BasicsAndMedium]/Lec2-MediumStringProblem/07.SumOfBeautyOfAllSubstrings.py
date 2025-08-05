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

class Solution:
    def beautySum(self, s: str) -> int:
        tot_b = 0
        for i in range(len(s)):
            freq = Counter()
            for j in range(i, len(s)):
                freq[s[j]] += 1
                tot_b += max(freq.values()) - min(freq.values())
        return tot_b