'''

'''


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        last =  self.fib(n-1)
        slast = self.fib(n-2)
        return last + slast
