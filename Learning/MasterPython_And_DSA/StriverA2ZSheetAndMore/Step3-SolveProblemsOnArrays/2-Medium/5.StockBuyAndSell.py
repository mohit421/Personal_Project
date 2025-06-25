'''
Link:- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Time complexity: O(n^2)

Space Complexity: O(1)
'''

# Solution 1 Brute force 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        maxi = 0
        for i in range(n):
            for j in range(i+1,n):
                profit = prices[j]-prices[i]
                maxi = max(profit, maxi)
        return maxi


# SOlution 2 Optimized one
'''
Complexity Analysis

Time complexity: O(n)

Space Complexity: O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mini = prices[0]
        maxPro = 0
        for i in range(n):
            cost = prices[i]-mini
            maxPro = max(maxPro,cost)
            mini  = min(mini, prices[i])
        return maxPro



# Above like

def maxProfit(arr):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro