'''
1- Reverse an Array
'''
# Solution 1
def printArr(ar):
    for i in range(len(ar)):
        print(ar[i],end=" ")
    print()

def revFunc(ar,l,r):
    if l>=r:
        return 
    ar[l],ar[r] = ar[r],ar[l]
    revFunc(ar,l+1,r-1)

if __name__ == "__main__":
    ar = list(map(int, input().split()))
    l = 0
    r = len(ar) -1
    revFunc(ar,l,r)
    printArr(ar)


# Solution 2

def revFunc1(i,ar):
    n = len(ar)
    if i>n//2:
        return 
    ar[i],ar[n-i-1] = ar[n-i-1],ar[i]
    revFunc1(i+1,ar)


if __name__ == "__main__":
    ar = list(map(int, input().split()))
    revFunc1(0,ar)
    printArr(ar)

