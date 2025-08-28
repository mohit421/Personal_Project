'''

'''



class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def pow(x,num):
            if num == 0:
                return 1
            res = 1
            while num>0:
                if num%2:
                    res = (res*x) % MOD
                num = num//2
                x = (x*x) % MOD
            return res
        
        even = ceil(n/2)
        odd = n//2

        return (pow(5, even) * pow(4, odd)) % MOD