'''

'''
# Solution 1
'''
Complexity
Time complexity:O(n)
Where n is the length of the string s. The in operator takes O(n) time in average case for substring search.
Space complexity:O(n)
Due to the concatenated string s +
'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        concat = s + s
        if goal in concat:
            return True
        return False
        

# ANother ways

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return (s+s).find(goal) != -1