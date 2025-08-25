'''

'''


# Without Memoization

'''
TC:- O(2^n) exponential in nature

'''

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    


# Using memoization in recursion

class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def recur_fib(N):
            if N in cache:
                return cache[N]
            if N<2:
                result= N
            else:
                result = recur_fib(N-1) + recur_fib(N-2)
            cache[N] = result
            return result
        return recur_fib(n)