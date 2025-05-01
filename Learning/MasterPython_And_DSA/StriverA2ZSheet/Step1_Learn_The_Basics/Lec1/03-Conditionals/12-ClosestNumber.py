# Problem Link:- https://www.geeksforgeeks.org/problems/closest-number5728/1?&selectedLang=python3


# Solution 1:-

# Brute force asteps

'''class Solution:
    def closestNumber(self, n , m):
        # code here 
        if(m==0):
            return None
        distance = 0
        lower = n - distance
        higher = n + distance
        while True:
            if higher%m == 0 and lower % m == 0:
                return higher if abs(higher) > abs(lower) else lower
            elif higher%m==0:
                return higher
            elif lower % m == 0:
                return lower
            distance +=1
'''


# Solution 2 
# 
# Time Complexity: O(1) (Constant Time)

def closest_number_simple(n, m):
    if m == 0:
        return None  # Cannot divide by zero

    # Get the closest multiple of m using integer division
    q = n // m
    lower = m * q
    upper = m * (q + 1)

    # Calculate the distances from n
    dist_lower = abs(n - lower)
    dist_upper = abs(n - upper)

    # If distances are equal, return the one with higher absolute value
    if dist_lower == dist_upper:
        return upper if abs(upper) > abs(lower) else lower
    else:
        return lower if dist_lower < dist_upper else upper

'''
Here's a `README.md` file based on the explanation you've asked for:

```markdown
# Closest Number Algorithm

This repository explains how to find the closest number to a given integer `n` that is divisible by `m`, and if there are multiple numbers at the same distance, it returns the one with the largest absolute value.

### Problem Description
Given two integers `n` and `m`, we want to find the number closest to `n` that is divisible by `m`. If there is more than one such number, return the one with the maximum absolute value.

---

### Code Explanation

Let's break down the full logic line-by-line of the key code:

```python
return min(candidates, key=lambda x: (abs(n - x), -abs(x)))
```

We’ll explain it **with an example**:  
Let’s say:
```python
n = -15
m = 6
```

From earlier in the code:
```python
q = n // m        # -15 // 6 = -3
cand1 = m * q     # 6 * -3 = -18
cand2 = m * (q+1) # 6 * -2 = -12
cand3 = m * (q-1) # 6 * -4 = -24
candidates = [-18, -12, -24]
```

---

### 🔍 Full Line Breakdown

Now, let’s break down the line in question:

```python
return min(candidates, key=lambda x: (abs(n - x), -abs(x)))
```

---

#### 1. **`min(candidates, key=...)`**
- This part is asking:  
  > “From the list of `candidates` (`[-18, -12, -24]`), return the one with the *smallest value*, according to the rule I give you in `key=`.”

---

#### 2. **`lambda x: (abs(n - x), -abs(x))`**
- This is the rule (or key) used for comparison.  
- For each candidate `x`, it builds a **tuple** like this:

```python
(abs(n - x), -abs(x))
```

Which means:
- First: how close `x` is to `n`
- Second: if there’s a tie, prefer the one with **larger absolute value**

---

#### 3. **Evaluate the key for each candidate**

| x     | abs(n - x) = abs(-15 - x) | abs(x) | Key Tuple                  |
|--------|----------------------------|---------|-----------------------------|
| -18    | abs(-15 - (-18)) = 3       | 18      | (3, -18) ✅ |
| -12    | abs(-15 - (-12)) = 3       | 12      | (3, -12) |
| -24    | abs(-15 - (-24)) = 9       | 24      | (9, -24) |

---

#### 4. **Choose the minimum key tuple**
- Python compares the tuples **left to right**:
  - First, the smaller `abs(n - x)` wins.
  - If tied, the one with **higher abs(x)** wins because of `-abs(x)` being **more negative for smaller values**.

- Comparing:
  - (3, -18) vs (3, -12) → pick (3, -18) (since -18 < -12 → means 18 is larger than 12)
  - (3, -18) vs (9, -24) → pick (3, -18) (3 < 9)

✅ So **`min(...)` picks `-18`**

---

### 🟩 Final Output:

```python
return -18
```

---

### 📌 Summary:

This line means:
> “Give me the number from the list that is **closest to `n`**, and if there are multiple, give the one with the **highest absolute value**.”


```

'''