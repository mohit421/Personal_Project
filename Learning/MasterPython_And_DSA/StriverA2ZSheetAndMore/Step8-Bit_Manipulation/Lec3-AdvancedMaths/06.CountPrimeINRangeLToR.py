'''

'''


# Brute force

class Solution:
    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
        
    def countPrimes(self, L, R):
        cnt = 0
        for j in range(L, R + 1):   # inclusive range
            if self.isPrime(j):
                cnt += 1
        return cnt


# brute force version 2

#User function Template for python3
'''
Time Complexity: O((R-L+1)*sqrt(N)) where  R and L are the endpoints of the range in each query and N is the maximum value in range.


For each query, there is a loop that iterates through each number in the range [L, R) hence the number of iterations is R-L+1.
Inside the inner loop, for each number we iterate up to its square root to check for divisors hence determine if it is prime or not.
Space Complexity: O(Q)where Q is the number of queries. For each query, we save a count of prime numbers in the ans vector. Apart from this, only constant additional space is required to store the intermediate variables in checking if a number is prime or not.
'''
class Solution:
    def isPrime(self, n):
        cnt = 0
        for i in range(1, int(n**0.5)+1):
            if n%i==0:
                cnt += 1
                if n//i != i:
                    cnt += 1
        if cnt == 2:
            return True
        return False
        
    def countPrimes(self,L,R):
        #code here
        
        cnt = 0
        
        for j in range(L,R+1):
            if self.isPrime(j):
                cnt += 1
        return cnt
            

# Better solution


#User function Template for python3
'''
Time Complexity: O((R-L+1))
'''
class Solution:
    def isPrime(self, n):
        prime = [1]*(n+1)
        prime[0]= prime[1] = 0
        for i in range(2, int(n**0.5)+1):
            if prime[i] == 1:
                for j in range(i*i,n+1, i):
                    prime[j] = 0
        return prime
        
        
    def countPrimes(self,L,R):
        #code here
        
        cnt = 0
        ans = []
        prime = self.isPrime(1000000)
        for j in range(2, 1000001):
            cnt += prime[j]
            prime[j] = cnt
        return prime[R] - prime[L-1]
            