# Problem link:- https://www.geeksforgeeks.org/problems/find-index-1614919939--145853/1&selectedLang=python3

# Solution 1
arr = tuple(map(int, input().split()))
x = int(input())
print(arr.index(x))


# Solution 2
arr = tuple(map(int, input().split()))
x = int(input())
for i in range(len(arr)):
    if x == arr[i]:
        print(i)
        break
