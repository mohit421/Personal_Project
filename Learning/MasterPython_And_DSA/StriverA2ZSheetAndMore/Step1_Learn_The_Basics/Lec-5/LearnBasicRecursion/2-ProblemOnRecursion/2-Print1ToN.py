'''
Print :- 1...N

'''

'''
def print1N(i,N):
    
    if i>N:
        return
    print(i)
    print1N(i+1,N)

N = int(input())
print1N(1,N)


'''

'''
Print 1....N by using Backtrack

'''
def print1TN(i,N):
    if i<1:
        return
    print1TN(i-1,N)
    print(i)

N= int(input())
print1TN(N,N)