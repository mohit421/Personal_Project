'''
Prinitng one subsequences whose sum equal to geive n sum
'''

# Non functiona lway bcuz we use global varibale 

found = False  # Global variable to track if a valid subsequence has been found

def printSubEqK(ind, ds, s, sm, arr, n):
    global found  # Access the global variable
    
    # Base case: when we have reached the end of the array
    if ind == n:
        if s == sm and not found:
            print(*ds)  # Print the subsequence
            found = True  # Mark that we've found a valid subsequence
        return

    # Include the current element in the subsequence
    ds.append(arr[ind])
    s += arr[ind]

    # Recurse with the included element
    if not found:
        printSubEqK(ind + 1, ds, s, sm, arr, n)

    # Backtrack: exclude the current element from the subsequence
    s -= arr[ind]
    ds.pop()

    # Recurse without the current element
    if not found:
        printSubEqK(ind + 1, ds, s, sm, arr, n)

# Example usage:
arr = [3, 5, 6, 7, 4, 2]
n = len(arr)
sm = 9
printSubEqK(0, [], 0, sm, arr, n)


# Solution 2

# Functional recursion way

def printSubEqK(ind, ds, s, sm, arr, n):

    # Base case: when we have reached the end of the array
    if ind == n:
        if s == sm:
            print(*ds)  # Print the subsequence
            return True 
        return False 

    # Include the current element in the subsequence
    ds.append(arr[ind])
    s += arr[ind]

    # Recurse with the included element
    if printSubEqK(ind + 1, ds, s, sm, arr, n):
        return True

    # Backtrack: exclude the current element from the subsequence
    s -= arr[ind]
    ds.pop()

    # Recurse without the current element
    if printSubEqK(ind + 1, ds, s, sm, arr, n):
        return True
    return False
# Example usage:
arr = [3, 5, 6, 7, 4, 2]
n = len(arr)
sm = 9
printSubEqK(0, [], 0, sm, arr, n)

