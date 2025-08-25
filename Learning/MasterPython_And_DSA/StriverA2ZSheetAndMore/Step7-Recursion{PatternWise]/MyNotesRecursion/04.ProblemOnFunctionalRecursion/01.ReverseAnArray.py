'''

'''


# Using two pointer aproach and recursion 


def reverse(arr,left, right):
    if left>= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left+1, right-1)
    return arr


def main():
    n = int(input())
    arr = arr = list(map(int, input().split()))
    print(*reverse(arr,0,n-1))

if __name__ == "__main__":
    main()


# Using one variable variable and recursion

def reverse(arr,i=0):
    n = len(arr)
    if i>= n//2:
        return arr
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    reverse(arr,i+1)
    return arr


def main():
    arr = list(map(int, input().split()))
    print(*reverse(arr))

if __name__ == "__main__":
    main()

