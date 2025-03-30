"""
🔹 Method 1: Convert to String & Sort Digits
"""
num = 50321

# Convert number to string and sort digits
sorted_str = "".join(sorted(str(num)))

print(sorted_str)  # Output: "01235"


"""
✅ str(num) → Converts the number to a string
✅ sorted(str(num)) → Sorts digits as a list of characters
✅ "".join(...) → Joins sorted characters back into a string"""

# 🔹 Method 2: Convert to Integer After Sorting

num = 50321

# Convert number to string, sort digits, and convert back to int
sorted_num = int("".join(sorted(str(num))))

print(sorted_num)  # Output: 1235
"""
🔹 This ensures the result is an integer instead of a string.
🔹 Method 3: Sort in Descending Order"""
num = 50321

sorted_desc = int("".join(sorted(str(num), reverse=True)))

print(sorted_desc)  # Output: 53210
# 🔹 reverse=True sorts digits in descending order.