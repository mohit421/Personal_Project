'''

'''

# soLUTION
'''
Time Complexity: O( (2^n) *k*(n/2) )

Reason: O(2^n) to generate every substring and O(n/2)  to check if the substring generated is a palindrome. O(k) is for inserting the palindromes in another data structure, where k  is the average length of the palindrome list.

Space Complexity: O(k * x)

Reason: The space complexity can vary depending on the length of the answer. k is the average length of the list of palindromes and if we have x such list of palindromes in our final answer. The depth of the recursion tree is n, so the auxiliary space required is equal to the O(n).
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        lst = []

        def helper(ind):
            if ind==len(s):
                res.append(lst[:])
                return

            for i in range(ind, len(s)):
                if isPalindrome(s,ind,i):
                    lst.append(s[ind:i+1])
                    helper(i+1)
                    lst.pop()
        
        def isPalindrome(s,start,end):
            while start<=end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -=1 
            return True

        helper(0)
        return res