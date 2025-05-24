'''
3005. Count Elements with Maximum Frequency
Link:- https://leetcode.com/problems/count-elements-with-maximum-frequency/description/


Complexity
Time complexity:
O(n+m) where m=∣freq∣≤max(nums)≤100

Space complexity:
O(m)
'''

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0]*101
        maxF = 0
        for a in nums:
            freq[a] += 1
            maxF = max(maxF,freq[a])
        ans = 0
        for f in freq:
            if f==maxF:
                ans += f
        return ans
    

# Solution 2

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        c = 0
        for x in nums:
            if str(x) in d:
                d[str(x)] += 1
            else:
                d[str(x)] = 1
        for freq in d.values():
            if freq == max(d.values()):
                c += freq
        return c
    

# Solution 3
'''

Suppose:

python

nums = [1, 2, 2, 3, 1, 4]
1 occurs 2 times

2 occurs 2 times

3 and 4 occur once

The maximum frequency is 2, and both 1 and 2 have that frequency.
So the total number of such elements is: 2 (from 1) + 2 (from 2) = 4
Step-by-step Explanation:
1. count = Counter(nums)
This counts how many times each number appears.

Output (for example): Counter({1: 2, 2: 2, 3: 1, 4: 1})

2. max_frequency = max(count.values())
This finds the highest frequency value.

Example: max_frequency = 2

3. Loop through count.values():
python

for i in count.values():
    if i == max_frequency:
        c += i
Adds up all frequencies that are equal to the max frequency.

So if two numbers each appear 2 times, c = 2 + 2 = 4

4. return c
Returns the total count of numbers that appear with maximum frequency
'''
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        c = 0
        max_frequency = max(count.values())

        for i in count.values():
            if i == max_frequency:
                c += i
        return c