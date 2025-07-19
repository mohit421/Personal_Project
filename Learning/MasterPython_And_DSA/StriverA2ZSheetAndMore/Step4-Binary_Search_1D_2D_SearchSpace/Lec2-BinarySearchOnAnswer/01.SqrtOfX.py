'''

'''
# Solution 1 Using linear search


def mySqrt(n):
    ans = 0
    # Linear search on the answer space:
    for i in range(1, n+1):
        val = i * i
        if val <= n:
            ans = i
        else:
            break
    return ans



# Solution 2

def floorSqrt(n):
    ans = int(math.sqrt(n))
    return ans




# Solution 3 using binary search



class Solution:
    def mySqrt(self, x: int) -> int:
        lo,hi = 1, x
        ans = 1
        while lo<=hi:
            mid = (lo+hi)//2
            if (mid*mid) <= x:
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        # return ans
        return hi
            
    
