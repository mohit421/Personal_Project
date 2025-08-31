'''
Print count of subsequences whose sum is equal to given sum

'''


def printSubEqK(ind, s, sm, arr, n):

    # Base case: when we have reached the end of the array
    if ind == n:
        if s == sm:
            return 1
        return 0

    # Include the current element in the subsequence
    s += arr[ind]

    # Recurse with the included element
    l = printSubEqK(ind + 1, s, sm, arr, n)

    # Backtrack: exclude the current element from the subsequence
    s -= arr[ind]

    # Recurse without the current element
    r = printSubEqK(ind + 1, s, sm, arr, n)
    return l + r
# Example usage:
arr = [3, 5, 6, 7, 4, 2]
n = len(arr)
sm = 9
print(printSubEqK(0, 0, sm, arr, n))

