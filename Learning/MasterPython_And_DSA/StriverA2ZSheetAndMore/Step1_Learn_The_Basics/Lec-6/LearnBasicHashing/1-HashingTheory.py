'''
TC:- O(Q*N)
'''

def nonHashingWay(n,ar):
    cnt= 0
    for i in range(n):
        if ar[i] == n:
            cnt += 1

    return cnt 

n = int(input())
ar = list(map(int,input().split()))

hashing(n,ar)