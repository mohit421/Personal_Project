'''

'''

# Solution 1 using Counter method

'''
Time Complexity:
Counter(s) → O(n), where n is the length of string s

Counter(t) → O(n), where n is the length of string t

Comparing the two counters → O(1) on average (since character set is bounded, e.g., lowercase letters)

In worst case (unbounded character set), it's O(k), where k is the number of unique characters.

✅ Overall Time Complexity: O(n)
'''
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Using sorted method
'''
🔍 Time Complexity:
sorted(s) → O(n log n)

sorted(t) → O(n log n)

Comparing the two lists → O(n)

✅ Overall Time Complexity: O(n log n)


'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

# Wihout Built-in
'''
⏱️ Time & Space Complexity:
Time Complexity: O(n) – we traverse both strings once and loop through a fixed array.

Space Complexity: O(1) – constant space (only 26 integers).
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    return False

        freq = [0]*26

        for ch in s:
            freq[ord(ch)- ord('a')] += 1
        for ch in t:
            freq[ord(ch)- ord('a')] -= 1
        
        for count in freq:
            if count != 0:
                return False
        return True
    
#  Wighout builit in optimised one

'''
 Time and Space Complexity:
Measure	Value
Time Complexity	O(n)
Space Complexity	O(1) (fixed array of 26 ints)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    return False

        freq = [0]*26

        for ch in range(len(s)):
            freq[ord(s[ch])- ord('a')] += 1
            freq[ord(t[ch])- ord('a')] -= 1
        
        for count in freq:
            if count != 0:
                return False
        return True