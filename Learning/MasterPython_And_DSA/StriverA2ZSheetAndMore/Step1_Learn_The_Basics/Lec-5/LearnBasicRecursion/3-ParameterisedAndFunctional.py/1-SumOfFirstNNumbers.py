'''
Sum of first N number:- 


'''

# Parameterised Solution

def sumFirstN(i,sum):
    if i<1:
        print(sum)
        return 
    sumFirstN(i-1,sum+i)


n = int(input())
sumFirstN(n,0)