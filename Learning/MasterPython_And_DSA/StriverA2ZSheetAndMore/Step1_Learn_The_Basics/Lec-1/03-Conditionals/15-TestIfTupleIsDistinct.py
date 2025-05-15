# Problem link:- https://www.geeksforgeeks.org/problems/test-if-tuple-is-distinct/1?&selectedLang=python3

# Solution 1
#User function Template for python3
arr = tuple(map(int, input().split()))

def all_unique(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return False
        seen.add(item)
    return True

print(all_unique(arr))

# Solution 2
arr = tuple(map(int, input().split()))


aset = set(arr)
lenA = len(aset)
lenArr = len(arr)
if lenA==lenArr:
    print(True)
else:
    print(False)


# Solution 3  Using List Comprehension and count()
def all_unique(arr):
    return all(arr.count(x) == 1 for x in arr)


# Solution 4   Using collections.Counter

from collections import Counter

def all_unique(arr):
    return all(count == 1 for count in Counter(arr).values())

'''

'''

# Solution 5 Functional Style with map() and filter()

def all_unique(arr):
    return not list(filter(lambda x: arr.count(x) > 1, arr))
