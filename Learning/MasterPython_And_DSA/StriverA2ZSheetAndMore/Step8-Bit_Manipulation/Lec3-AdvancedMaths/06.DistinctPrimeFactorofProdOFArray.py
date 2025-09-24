'''
Distinct prime factor of a product of an array
'''

# Brute force 

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:  # 2 is prime
                return True
            if n % 2 == 0:  # even numbers > 2 are not prime
                return False
            for i in range(3, int(n**0.5) + 1, 2):  # check odd divisors only
                if n % i == 0:
                    return False
            return True
        
        cnt = 0
        mult = 1
        for i in range(len(nums)):
            mult *= nums[i]
        for i in range(2,mult+1):
            if mult%i == 0:
                if is_prime(i):
                    cnt += 1
        return cnt