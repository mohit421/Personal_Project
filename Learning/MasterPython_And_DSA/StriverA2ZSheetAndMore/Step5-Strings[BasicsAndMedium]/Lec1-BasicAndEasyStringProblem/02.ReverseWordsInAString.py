'''

'''
# Brute force using stack
# Will do once reached stack 



# Using Two pointer appraoch Optimised solution
'''
Time Complexity: O(N), N~length of string

Space Complexity: O(1), Constant Space
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s)-1

        temp = ""
        ans = []

        while left<=right:
            ch  = s[left]
            if ch != ' ':
                temp += ch
            else:
                if temp:
                    ans.insert(0,temp)
                    temp = ""
            left += 1
        if temp:
            ans.insert(0,temp)
        return ' '.join(ans)
    

# Using built in functions 
'''
Time Complexity:
O(n)
(Each character is processed a constant number of times)

Space Complexity:
O(n)
(Due to intermediate strings and list of words)



Step-by-step Breakdown:
s.strip()

Removes leading and trailing spaces.

Time Complexity: O(n)

Space Complexity: O(n) (since strings are immutable, a new string is created)

.split()

Splits the string into words using whitespace.

Automatically handles multiple spaces.

Time Complexity: O(n) (each character is read once)

Space Complexity: O(w), where w is the number of words (each word stored in a list)

reversed(words)

Reverses the list of words (creates a reverse iterator).

Time Complexity: O(w)

Space Complexity: O(1) for iterator; O(w) when joined later

' '.join(...)

Joins the words into a single string with a space separator.

Total characters joined will again be O(n).

Time Complexity: O(n)

Space Complexity: O(n)


'''
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return ' '.join(reversed(words))
