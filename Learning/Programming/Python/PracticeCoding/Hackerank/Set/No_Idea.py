# How to take user input in python  in different different ways



"""
Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

---

### 🧾 **Problem Recap (Input format):**
```
Line 1: n k (two integers)
Line 2: array of n integers
Line 3: k integers (b)
Line 4: k integers (c)
```

---

## ✅ **1. Basic & Readable**
```python
n, k = map(int, input().split())
arr = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
```

---

## ⚡️ **2. One-liner Style (short, fast)**
```python
n, k, arr, b, c = *map(int, input().split()), list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
```
> ⚠️ Not very readable — use for flexing or when you're comfy.

---

## 🌀 **3. Using List Comprehension to Handle All Input at Once**
```python
data = [list(map(int, input().split())) for _ in range(4)]
n, k = data[0]
arr = data[1]
b = data[2]
c = data[3]
```

---

## 🧠 **4. Using sys.stdin for Speed (for huge input cases)**
```python
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
```

> Faster than `input()` in large input cases like contests.

---

## 💎 **5. Read All at Once and Slice**
```python
all_data = list(map(int, open(0).read().split()))
n, k = all_data[0], all_data[1]
arr = all_data[2:2+n]
b = all_data[2+n:2+n+k]
c = all_data[2+n+k:2+n+2*k]
```

> Super useful when HackerRank dumps everything at once and you don’t want to call `input()` multiple times.

---

"""

# Code

# Solution 1

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)


# Solution 2

print(sum((i in A) - (i in B) for i in arr))

# Solution 3

from collections import Counter

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

count = Counter(arr)

happiness = sum(count[x] for x in A) - sum(count[x] for x in B)
print(happiness)


# Solution 4

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A, B = set(map(int, input().split())), set(map(int, input().split()))

print(sum(map(lambda x: 1 if x in A else -1 if x in B else 0, arr)))
