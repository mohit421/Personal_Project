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
'''
Time Complexity: O(n), single-pass involved.

Space Complexity: O(1) 
'''
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

# Solution 3
def reverseArray(arr, n):
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    printArray(arr, n)

# Driver Code
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)


# Solution 4

'''
Time Complexity: O(n)

Space Complexity: O(1)
'''
def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


def reverseArray(arr, n):
    arr.reverse()


# Driver Code
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)
    printArray(arr, n)



# Solution 5
'''
Time Complexity: O(n), single-pass for reversing array.

Space Complexity: O(n), for the extra array used.
'''
def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


def reverseArray(arr, n):
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        ans[n - i - 1] = arr[i]
    printArray(ans, n)


# Driver Code
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)