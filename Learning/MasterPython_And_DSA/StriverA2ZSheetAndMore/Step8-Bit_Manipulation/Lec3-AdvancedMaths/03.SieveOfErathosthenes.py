'''

'''

# Brute force

class Solution:
    def countPrimes(self, n: int) -> int:
        def is_prime(n:int)->bool:
            if n<=1:
                return False
            if n<=3:
                return True
            if n%2 ==0 or n%3 == 0:
                return False
            for i in range(5,int(math.sqrt(n))+1,6):
                if n%i==0 or n%(i+2) == 0:
                    return False
            return True
        cnt = 0
        for i in range(2,n):
            if is_prime(i):
                cnt += 1
        return cnt
    

# Optimal SOlution

class Solution:
    def countPrimes(self, n: int) -> int:

        prime = [1]*(n+1)
        for i in range(2,n):
            if prime[i] == 1:
                for j in range(2*i,n,i):
                    prime[j] = 0
        cnt = 0
        for i in range(2,n):
            if prime[i] == 1:
                cnt += 1
        return cnt
    


# Most optimal soltuion
'''
Prime harmonic series
TC:- O(N) +  (Nlog(logN)) + O(N)
SC:- O(N)
'''
class Solution:
    def countPrimes(self, n: int) -> int:

        prime = [1]*(n+1)
        for i in range(2,int(n**0.5)+1):
            if prime[i] == 1:
                for j in range(i*i,n,i):
                    prime[j] = 0
        cnt = 0
        for i in range(2,n):
            if prime[i] == 1:
                cnt += 1
        return cnt