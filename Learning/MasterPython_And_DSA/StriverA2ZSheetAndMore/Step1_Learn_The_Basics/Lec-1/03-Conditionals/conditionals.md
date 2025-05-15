# Match-Case Statement in Python

- match-case statement is Python's version of a switch-case found in other languages. It allows us to match a variable's value against a set of patterns.

```
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")


```

Of course! 🚀  
Here’s a clean, full **`README.md`** notes file for **Conditionals in Python**:

---

# 📘 Conditionals in Python

Conditionals are used to **make decisions** in a Python program.  
They allow code to **run differently** depending on whether a condition is `True` or `False`.

---

## 🛠 Types of Conditional Statements

### 1. `if` Statement

Executes a block of code **if** the condition is true.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

### 2. `if-else` Statement

Provides an **alternative block** if the condition is false.

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
```

---

### 3. `if-elif-else` Chain

Checks **multiple conditions** in order.

```python
x = 5

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is exactly 5")
else:
    print("x is less than 5")
```

- `elif` stands for "**else if**"
- Python checks conditions **top-down**, and stops at the **first True** one.

---

### 4. Nested `if` Statements

An `if` block inside another `if`.

```python
x = 10

if x > 5:
    if x < 15:
        print("x is between 5 and 15")
```

✅ Good for **multi-level decision making**.

---

## 🧠 Logical Operators with Conditionals

You can combine multiple conditions using:

| Operator | Meaning                        | Example               |
| :------- | :----------------------------- | :-------------------- |
| `and`    | Both conditions must be True   | `if a > 0 and b > 0:` |
| `or`     | At least one condition is True | `if a > 0 or b > 0:`  |
| `not`    | Reverses the condition         | `if not a > 0:`       |

Example:

```python
a = 5
b = 7

if a > 0 and b > 0:
    print("Both are positive")
```

---

## 📌 Important Notes

- Python uses **indentation (4 spaces)** to define code blocks.
- Conditions must be **boolean expressions** (evaluate to True or False).
- Always use **:` (colon)** at the end of `if`, `elif`, and `else` lines.

---

## 🚀 Short-Hand If and If-Else

### Short-Hand `if`

```python
x = 5
if x > 0: print("Positive")
```

### Short-Hand `if-else` (Ternary Operator)

```python
x = 5
print("Positive" if x > 0 else "Non-positive")
```

✅ Great for writing **compact** code.

---

# 🎯 Example Full Program

```python
x = int(input("Enter a number: "))

if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")
```

---

# 📚 Summary Table

| Statement       | Use                        |
| :-------------- | :------------------------- |
| `if`            | Check a condition          |
| `if-else`       | Two-way decision           |
| `if-elif-else`  | Multiple conditions        |
| `nested if`     | Decision inside a decision |
| `short-hand if` | Single-line condition      |

---

# ✨ Happy Learning Python! ✨

---
