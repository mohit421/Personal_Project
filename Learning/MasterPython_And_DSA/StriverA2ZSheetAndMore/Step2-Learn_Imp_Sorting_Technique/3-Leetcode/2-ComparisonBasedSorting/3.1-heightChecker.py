#Using bubble sort 

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        has_swapped = True
        lst = heights[:]
        while has_swapped:
            has_swapped = False
            for i in range(len(heights)-1):
                if heights[i]> heights[i+1]:
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                    has_swapped = True
        count = 0
        for i in range(len(lst)):
            if lst[i] != heights[i]:
                count += 1
        return count
        