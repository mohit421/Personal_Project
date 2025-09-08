# Bit Manipulation

- Binary Number Conversion (1's & 2's Compliment)
- Operators (AND, OR, XOR, NOT, Shift)
- Swap 2 Numbers
- Checks if the ith bit is set or not
- Extract the ith bit
- set the ith bit
- clear the ith bit
- toggle the ith bit

## Convert Decimal to Binary

### 1. Introduction

- Decimal system: Base-10, digits from 0–9.
- Binary system: Base-2, digits only 0 and 1.
- Converting decimal → binary is fundamental in computer architecture, DSA, and low-level programming.
- Computers internally represent all numbers in binary (bits), so conversion is often done using bit manipulation.

#### Example (Division by 2 method)

```
13 ÷ 2 = 6 remainder 1
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1
Binary = 1101
```

### 2. Code

```python
def convertToBinary(n: int) -> str:
    if n == 0:
        return "0"
    res = []
    while n > 0:
        if n % 2 == 1:
            res.append("1")
        else:
            res.append("0")
        n //= 2   # integer division

    # reverse because we collected bits from LSB to MSB
    return "".join(reversed(res))

print(convertToBinary(13)) # Output: "1101"
print(convertToBinary(5))  # Output: "101"
print(convertToBinary(0))  # Output: "0"
```

## Convert Binary TO Decimal

```python

#TC:- O(len)
#SC: O(1)

def convertToDecimal(x):
    l = len(x)
    p2 = 1
    num = 0
    for i in range(l-1,-1,-1):
        if x[i] == '1':
            num = num + p2
        p2 = p2*2
    return num

print(convertToDecimal("1101"))
```

# 1's and 2's Complement

## 1. Introduction

- **1's complement** and **2's complement** are methods of representing negative numbers in binary.
- They are widely used in computer systems to handle signed integers.

---

## 2. 1's Complement

- To get the **1's complement** of a binary number, invert all the bits (0 → 1, 1 → 0).

### Example:

```
Binary:   0101 (5 in decimal)
1's comp: 1010 (-5 in 1's complement representation)
```

### Properties:

- Range: For `n` bits → from `-(2^(n-1)-1)` to `+(2^(n-1)-1)`
- Has **two representations for zero** (+0 and -0).

---

## 3. 2's Complement

- To get the **2's complement**:
  1. Take the 1's complement.
  2. Add 1 to the least significant bit (LSB).

### Example:

```
Binary:     0101 (5 in decimal)
1's comp:   1010
+1:         1011  (-5 in 2's complement representation)
```

### Properties:

- Range: For `n` bits → from `-2^(n-1)` to `+(2^(n-1)-1)`
- Only **one representation for zero**.
- Most common system for signed integers in computers.

---

## 4. Comparison

| Feature             | 1's Complement               | 2's Complement           |
| ------------------- | ---------------------------- | ------------------------ |
| Method              | Invert bits                  | Invert + add 1           |
| Zero representation | Two (+0, -0)                 | One unique zero          |
| Range (n bits)      | -(2^(n-1)-1) to +(2^(n-1)-1) | -2^(n-1) to +(2^(n-1)-1) |
| Hardware usage      | Rarely used                  | Standard in modern CPUs  |

---

## 5. Python Example

```python
def ones_complement(n: int, bits: int) -> str:
    mask = (1 << bits) - 1
    return format(~n & mask, f"0{bits}b")

def twos_complement(n: int, bits: int) -> str:
    mask = (1 << bits) - 1
    return format((~n + 1) & mask, f"0{bits}b")

# Example usage
print("1's complement of 5 (4 bits):", ones_complement(5, 4))  # 1010
print("2's complement of 5 (4 bits):", twos_complement(5, 4))  # 1011
```

---

## 6. Key Takeaways

- **1's complement**: invert all bits.
- **2's complement**: invert all bits + add 1.
- **2's complement is preferred** in modern systems because of unique zero and simpler arithmetic.

# Bitwise Operators in Python

## 1. Introduction

- Bitwise operators work directly on the binary representation of integers.
- They are commonly used in low-level programming, optimization, cryptography, and computer architecture.

---

## 2. Bitwise AND (`&`)

- Compares each bit of two numbers.
- Result is `1` if **both bits are 1**, else `0`.

### Example:

```
5 = 0101
3 = 0011

5 & 3 = 0001 (1 in decimal)
```

---

## 3. Bitwise OR (`|`)

- Compares each bit of two numbers.
- Result is `1` if **at least one bit is 1**, else `0`.

### Example:

```
5 = 0101
3 = 0011

5 | 3 = 0111 (7 in decimal)
```

---

## 4. Bitwise XOR (`^`)

- Compares each bit of two numbers.
- Result is `1` if **bits are different**, else `0`.

### Example:

```
5 = 0101
3 = 0011

5 ^ 3 = 0110 (6 in decimal)
```

---

## 5. Bitwise NOT (`~`)

- Inverts all bits (0 → 1, 1 → 0).
- In Python, numbers are stored in 2's complement format for negatives.
- Formula: `~n = -(n+1)`

### Example:

```
5 = 0101
~5 = ...1010 (-6 in decimal)
```

---

## 6. Left Shift (`<<`)

- Shifts bits to the **left**, filling with zeros.
- Equivalent to multiplying by `2^k`.

### Example:

```
5 = 0000 0101
5<<1= 0000 1010 (10 in decimal)
5<<2= 0001 0100 (20 in decimal)
```

---

## 7. Right Shift (`>>`)

- Shifts bits to the **right**.
- Equivalent to integer division by `2^k`.

### Example:

```
20 = 0001 0100
20>>1= 0000 1010 (10 in decimal)
20>>2= 0000 0101 (5 in decimal)
```

---

## 8. Python Examples

```python
a, b = 5, 3

print("a & b =", a & b)   # 1
print("a | b =", a | b)   # 7
print("a ^ b =", a ^ b)   # 6
print("~a =", ~a)         # -6

print("a << 1 =", a << 1) # 10
print("a >> 1 =", a >> 1) # 2



9. Key Takeaways

AND (&): Both bits must be 1.

OR (|): At least one bit must be 1.

XOR (^): Bits must be different.

NOT (~): Inverts all bits (works with 2’s complement).

Left Shift (<<): Multiply by powers of 2.

Right Shift (>>): Divide by powers of 2 (integer division).
```

# Bit Manipulation: Set and Clear i-th Bit

## 1. Introduction

In bit manipulation, we often need to **set (turn on)** or **clear (turn off)** a specific bit in a number.  
This is done using **bitwise operators** with masks.

---

## 2. Setting the i-th Bit

- To **set the i-th bit** (make it `1`), we use the bitwise **OR** (`|`) operator.
- Formula:

n | (1 << i)

where `i` is the position of the bit (0-based index).

### Example:

```

n = 5 (0101 in binary)
i = 1

1 << i = 0010
n | (1 << i) = 0101 | 0010 = 0111 (7 in decimal)


```

### Code

Python code:

```python
def set_ith_bit(n: int, i: int) -> int:
    return n | (1 << i)

print(set_ith_bit(5, 1))  # 7
print(set_ith_bit(5, 2))  # 5 (already set)

```

#### Clearing the i-th Bit

To clear the i-th bit (make it 0), we use the bitwise AND (&) operator with the complement of the mask.

Formula:
n & ~(1 << i)

n = 5 (0101 in binary)
i = 2

1 << i = 0100
~(1 << i) = ...1011 (two's complement representation)
n & ~(1 << i) = 0101 & 1011 = 0001 (1 in decimal)

#### Examples

def clear_ith_bit(n: int, i: int) -> int:
return n & ~(1 << i)

print(clear_ith_bit(5, 2)) # 1
print(clear_ith_bit(5, 0)) # 4

```


### Removing the last set bit

# Bit Manipulation: Removing the Last Set Bit

## 1. Introduction
In bit manipulation, a common trick is **removing the rightmost (last) set bit** in a binary number.
This is done using the formula:

n & (n - 1)


---

## 2. Why Does It Work?

- Subtracting 1 from a number flips all bits **after the rightmost set bit**, including the rightmost set bit itself.
- AND-ing the result with the original number clears that bit and leaves the rest unchanged.

---

## 3. Example Walkthrough
```

### Example 1

n = 12 (1100 in binary)
n - 1 = 11 (1011 in binary)

n & (n - 1) = 1100 & 1011 = 1000 (8 in decimal)

✅ The last set bit (2^2) was removed.

### Example 2

n = 10 (1010 in binary)
n - 1 = 9 (1001 in binary)

n & (n - 1) = 1010 & 1001 = 1000 (8 in decimal)

✅ The last set bit (2^1) was removed.

---

## 4. Python Implementation

```python
def remove_last_set_bit(n: int) -> int:
    return n & (n - 1)

# Examples
print(remove_last_set_bit(12))  # 8
print(remove_last_set_bit(10))  # 8
print(remove_last_set_bit(7))   # 6 (111 -> 110)


5. Applications

Counting the number of set bits (Brian Kernighan’s Algorithm).

Checking if a number is a power of 2 (n > 0 and n & (n-1) == 0).

Efficiently iterating through subsets in combinatorics problems.

. Key Takeaways

Formula: n & (n - 1) removes the last set bit.

Useful for set bit counting and power of 2 checks.

Time complexity of repeated removal is O(number of set bits).

```

### Check if the numbner is power of 2 or not

```
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n & (n-1) == 0:
            return True
        return False


```
