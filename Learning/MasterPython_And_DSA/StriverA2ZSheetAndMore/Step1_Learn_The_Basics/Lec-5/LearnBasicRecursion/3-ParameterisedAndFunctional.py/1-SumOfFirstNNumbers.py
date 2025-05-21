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



# Functional 
def sumFirstN1(n):
    if n == 0:
        return 0
    return n + sumFirstN1(n-1)

n = int(input("Please enter ur no.: "))
print(sumFirstN1(n))