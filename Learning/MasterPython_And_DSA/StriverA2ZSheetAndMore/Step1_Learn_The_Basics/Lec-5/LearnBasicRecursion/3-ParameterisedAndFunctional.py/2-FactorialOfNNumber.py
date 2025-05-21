# Factorial of N


# Functiona Recursion


'''
TC:- O(N)

'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

n = int(input("Give ur no.: "))
print(fact(n))



# Paramterised Recursion

def fact1(i,f):
    if i < 1:
        print(f)
        return 
    fact1(i-1,f*i)

i = int(input())
fact1(i,1)
    
