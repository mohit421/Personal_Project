''''

'''

# Brute force
'''
Complexity Analysis

Time Complexity: O(N*sqrt(N)) where N is the input number. We iterate through numbers from 2 to n and inside the loop, we check if a number's factor is prime or not. To check that, we iterate up to the square root of it giving it a complexity of sqrt(N).

Space Complexity : O(sqrt(N))as the space used by the algorithm depends upon the size of the list to store the prime factors of N. In the worst case, the number of factors if N can be the square root of N.
'''
class Solution:
    
    def isPrime(self,n):
        cnt = 0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                cnt += 1
                if n//i != i:
                    cnt += 1
        
        if cnt == 2:
            return True
        return False
    
    def primeFac(self, n):
        # code here
        uniPrime = []
        for i in range(2,n+1):
            if n%i==0:
                if self.isPrime(i):
                    uniPrime.append(i)
        # uniPrime.sort()
        return uniPrime
        
    
# better solution version 1
'''
Complexity Analysis

Time Complexity: O(2*N)where N is the input number. The loop iterates up to the square root of n check if the factor is prime or not.

This complexity arises from the loop iterating up to the square root of N and performing operations to check if each factor and its divisor are prime. Within each iteration, two operations with a complexity of O(sqrt(N)) are performed.
Overall time complexity: O(sqrt(N)*2*sqrt(N)) = O(2*N).
Space Complexity : O(sqrt(N)) as the space used by the algorithm depends upon the size of the list to store the prime factors of N. In the worst case, the number of factors if N can be the square root of N.
'''
class Solution:
    
    def isPrime(self,n):
        cnt = 0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                cnt += 1
                if n//i != i:
                    cnt += 1
        
        if cnt == 2:
            return True
        return False
    
    def primeFac(self, n):
        # code here
        uniPrime = []
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                if self.isPrime(i) and i not in uniPrime:
                    uniPrime.append(i)
                if n//i != i:
                    if self.isPrime(n//i) and n//i not in uniPrime:
                        uniPrime.append(n//i)
        if self.isPrime(n) and n not in uniPrime:
            uniPrime.append(n)

        return uniPrime
        

#  better solution version 2 usaing set
'''
Complexity Analysis

Time Complexity: O(2*N)where N is the input number. The loop iterates up to the square root of n check if the factor is prime or not.

This complexity arises from the loop iterating up to the square root of N and performing operations to check if each factor and its divisor are prime. Within each iteration, two operations with a complexity of O(sqrt(N)) are performed.
Overall time complexity: O(sqrt(N)*2*sqrt(N)) = O(2*N).
Space Complexity : O(sqrt(N)) as the space used by the algorithm depends upon the size of the list to store the prime factors of N. In the worst case, the number of factors if N can be the square root of N.
'''
class Solution:
    
    def isPrime(self,n):
        cnt = 0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                cnt += 1
                if n//i != i:
                    cnt += 1
        
        if cnt == 2:
            return True
        return False
    
    def primeFac(self, n):
        # code here
        uniPrime = set()
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                if self.isPrime(i):
                    uniPrime.add(i)
                if n//i != i:
                    if self.isPrime(n//i):
                        uniPrime.add(n//i)
        if self.isPrime(n):
            uniPrime.add(n)

        return sorted(uniPrime)
        
    




    
# Solution 3
class Solution:

    def primeFac(self, n):
        # code here
        lst = []
        for i in range(2,n+1):
            if n%i==0:
                lst.append(i)
            while n%i==0:
                n = n//i
        
        return lst      
        
    
# most optmised solution

'''
TC:- O(sqrt(N)LogN)
'''
class Solution:
    

    
    def primeFac(self, n):
        # code here
        lst = []
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                lst.append(i)
                while n%i==0:
                    n = n//i
        if n>1:
            lst.append(n)
        return lst      
        
    