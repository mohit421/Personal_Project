'''
Prinitng all the subsequences whose sum equal to geive n sum
'''

# Solution 1


def printSubEqK(ind, ds, s, sm,arr, n):
    if ind == n:
        if s == sm:
            print(*ds)
        return

    ds.append(arr[ind])
    s += arr[ind]

    printSubEqK(ind + 1, ds,s, sm, arr,n)

    s -= arr[ind]
    ds.pop()

    printSubEqK(ind+1, ds, s, sm, arr, n)


arr = [3,5,6,7,4,2]
n = len(arr)
sm = 9
printSubEqK(0,[],0,sm, arr, n)


