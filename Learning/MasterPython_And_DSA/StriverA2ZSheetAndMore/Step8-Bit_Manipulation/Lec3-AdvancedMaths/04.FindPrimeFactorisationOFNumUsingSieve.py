'''

'''

# Brute  force

class Solution:
    def __init__(self, N=10**6):
        self.N = N
    
    def sieve(self):
        prime = [1] * (self.N + 1)
        prime[0] = prime[1] = 0
        for i in range(2, int(self.N**0.5) + 1):
            if prime[i]:
                for j in range(i * i, self.N + 1, i):
                    prime[j] = 0
        primes = [i for i in range(2, self.N + 1) if prime[i]]
        return primes

    def findPrimeFactors(self, N):
        factors = []
        primes = self.sieve()   # no argument
        for p in primes:
            if p * p > N:   # optimization: stop early
                break
            while N % p == 0:
                factors.append(p)
                N //= p
        if N > 1:
            factors.append(N)
        return factors


# Optimal 
'''
Fix: Precompute sieve once in __init__

Compute primes once when the object is created, and reuse them in every call.
'''

class Solution:
    def __init__(self, N=10**6):
        self.N = N
        self.primes = self.sieve()   # precompute once
    
    def sieve(self):
        prime = [1] * (self.N + 1)
        prime[0] = prime[1] = 0
        for i in range(2, int(self.N**0.5) + 1):
            if prime[i]:
                for j in range(i * i, self.N + 1, i):
                    prime[j] = 0
        return [i for i in range(2, self.N + 1) if prime[i]]

    def findPrimeFactors(self, N):
        factors = []
        for p in self.primes:
            if p * p > N:
                break
            while N % p == 0:
                factors.append(p)
                N //= p
        if N > 1:
            factors.append(N)
        return factors
