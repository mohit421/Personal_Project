'''
GCD
'''


# Eculidean ALgorrithm

'''
N1, N2

gcd(N1,N2) = gcd(N1-N2,N2)
gcd(a,b) = gcd(a-b,b) ---> 0    a>b

gcd(20,15) = gcd(5,15)

gcd(15,5) = gcd(10,5) = gcd(5,5) = gcd(0,5)
gcd(52,10) = gcd(42,10) = gcd(32,10) = gcd(22,10) = gcd(12,10) = gcd(2,10)

we can directly gone to last  gcd(2,10) by using modulus

gcd(a,b) = gcd(a%b,b)       ... a>b

Remember: greater % smaller

Time complexity:-
O(log(min(a,b))) :- log of phi of min(a,b)
'''
def gcd(a,b):
    while (a>0 and b>0):
        if a>b:
            a = a%b 
            b = b%a 
        if a==0:
            print(b,end='')
        else:
            print(a)






