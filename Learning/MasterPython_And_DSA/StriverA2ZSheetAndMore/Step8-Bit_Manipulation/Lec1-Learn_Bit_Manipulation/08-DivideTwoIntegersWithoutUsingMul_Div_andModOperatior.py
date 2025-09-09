'''

'''



# SOlution Optimal sol

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == divisor:
            return 1
        sign = True
        if dividend >= 0 and divisor <0:
            sign = False
        if dividend < 0 and divisor>=0:
            sign = False
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        while n>= d:
            cnt = 0
            while n>= (d<<(cnt+1)):
                cnt += 1
            
            ans += 1<<cnt
            n = n- (d*(1<<cnt))
        
        # Apply sign
        ans = ans if sign else -ans

        # Clamp to 32-bit signed int
        return max(min(ans, INT_MAX), INT_MIN)