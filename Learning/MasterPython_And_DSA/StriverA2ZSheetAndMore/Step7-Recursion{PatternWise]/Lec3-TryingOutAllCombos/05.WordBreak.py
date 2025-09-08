'''


'''


# SOlution 1 Iterative way using Dynamic programing

'''

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[len(s)]  = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]


# SOlution 2 Recursive way using memoization 

'''
Example 1 — s = "leetcode", wordDict = ["leet","code"] (expected: True)

Trace (indices in brackets refer to start):

Call dfs(0) (trying to split "leetcode").

Try end=1..4:

s[0:1]="l" → not in set

s[0:2]="le" → not in set

s[0:3]="lee" → not in set

s[0:4]="leet" → in set → call dfs(4).

Inside dfs(4) (suffix is "code"):

s[4:5]="c" → not in set

s[4:6]="co" → not in set

s[4:7]="cod" → not in set

s[4:8]="code" → in set → call dfs(8).

dfs(8) sees start == len(s) → return True.

dfs(4) receives True, sets memo[4] = True, returns True.

dfs(0) receives True, sets memo[0] = True, returns True.

Final memo (one valid trace): {4: True, 0: True}


dfs(0)
 └─ "leet" -> dfs(4)
     └─ "code" -> dfs(8) -> True




Example 2:
Example 2 — s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] (expected: False)

This example shows how memoization saves repeated work.

Indices: 0..8 (length 9).

dfs(0) for "catsandog":

s[0:3]="cat" is in set → call dfs(3).

dfs(3) (suffix "sandog"):

try substrings; s[3:7]="sand" is in set → call dfs(7).

dfs(7) (suffix "og"):

s[7:8]="o" not in set

s[7:9]="og" not in set
→ no valid split → set memo[7] = False, return False.

Back in dfs(3) continue:

no other valid splits produce True → set memo[3] = False, return False.

Back in dfs(0) continue:

s[0:4]="cats" is in set → call dfs(4).

dfs(4) (suffix "andog"):

s[4:7]="and" is in set → call dfs(7) → memo[7] exists False → dfs(7) immediately returns False (no recomputation).

dfs(4) finds no other success → set memo[4] = False, return False.

dfs(0) continues trying other ends end=5..9 — none produce True.

Set memo[0] = False, return False.

Key memo updates you'll see:

After first failing branch: memo[7] = False

Then memo[3] = False (from dfs(3))

Later memo[4] = False

Finally memo[0] = False

Because memo[7] was cached as False, the second time we need dfs(7) we skip re-searching the whole "og" suffix — big saving.

dfs(0)
 ├─ "cat" -> dfs(3)
 │    └─ "sand" -> dfs(7) -> False (memo[7]=False)
 └─ "cats" -> dfs(4)
      └─ "and" -> dfs(7) -> uses memo[7]=False

      

Time (with memo): roughly O(n²) in typical analyses because for each start you try up to O(n) end positions and substring checks cost up to O(n) in naïve slicing; in practice using word_set and limiting substring length reduces constants.

Time (without memo): exponential in worst case.

Space: O(n) for memo + recursion call stack up to depth n.
'''

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            for end in range(start+1, len(s)+1):
                if s[start:end] in word_set and dfs(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return dfs(0)
