# Enter your code here. Read input from STDIN. Print output to STDOUT

# Solution 1
'''
 How it works:
combinations_with_replacement(s, k) generates tuples of all possible combinations where elements can repeat and are picked in sorted order.

Example: For 'AC' and k=2 → possible: 'AA', 'AC', 'CC'

We join each tuple into a string before printing.

This is the most efficient and clean solution.
'''
from itertools import combinations_with_replacement

S,k = input().split()
K =int(k)
s= sorted(S)
# print(list(combinations_with_replacement(S,K)))

res = (list(map(lambda x: ''.join(x),sorted(combinations_with_replacement(s,K)))))
for cr in res:
    print(cr,sep='\n')


# Solution 2


'''
 
'''
from itertools import combinations_with_replacement

s, k = input().split()
s = ''.join(sorted(s))  # sort input string
k = int(k)

for combo in combinations_with_replacement(s, k):
    print(''.join(combo))


# Solution 3  Method 3: Using itertools.product + filtering

'''
How it works:
product(s, repeat=k) gives all possible k-length combinations (with repetition).

Then we filter out only the ones that are sorted, e.g. 'AC' is valid, 'CA' is not.

This is a bit less efficient than combinations_with_replacement, but still works well.
'''
from itertools import product

s, k = input().split()
s = ''.join(sorted(s))
k = int(k)

for p in product(s, repeat=int(k)):
    if list(p) == sorted(p):  # ensure it's in non-decreasing order
        print(''.join(p))



# Solution 4 Brute-force Nested Loops
''''
Method 4: Brute-force Nested Loops (only for small inputs)
This is not scalable for large k, but for learning purposes:

How it works:
Manual double-loop through the characters.

We avoid duplicates and preserve order by starting inner loop from i.
'''

'''
itertools.groupby() in Python
Last Updated : 21 Mar, 2025
The itertools.groupby() function in Python is part of the itertools module and is used for grouping consecutive elements of an iterable that have the same value. It generates a group of consecutive elements from an iterable and returns them as tuples containing a key and a group.

Example:




import itertools 

L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)] 

# Key function 
key_func = lambda x: x[0] 

for key, group in itertools.groupby(L, key_func): 
	print(key + " :", list(group)) 

Output
a : [('a', 1), ('a', 2)]
b : [('b', 3), ('b', 4)]
Explanation: In this code, itertools.groupby() groups the list of tuples based on the first element of each tuple. The key function (key_func) extracts the first element of each tuple (x[0]). The groupby() function then categorizes the tuples into groups with the same first element, and each group is displayed in the output.

Syntax
itertools.groupby(iterable, key=None)


Parameters
iterable: This is the iterable (like a list, tuple, string, etc.) whose elements are to be grouped.
key (optional): A function to compute a key value for each element. This is used for grouping, and by default, it is None. When None, the elements are grouped based on their actual value.
Return Value
The groupby() method returns an iterator of consecutive (key, group) pairs. Each group is itself an iterator, containing consecutive elements from the iterable that share the same key.

Examples of itertools.groupby()
1. Grouping Consecutive Even and Odd Numbers
This example demonstrates how to use itertools.groupby() to group consecutive numbers into even and odd categories.




import itertools

# List of numbers
a = [2, 4, 6, 7, 8, 10, 11, 12, 13]

# Grouping consecutive even and odd numbers
g_data = itertools.groupby(a, key=lambda x: 'Even' if x % 2 == 0 else 'Odd')

# Display grouped elements
for key, group in g_data:
    print(f"Group: {key} -> {list(group)}")

Output
Group: Even -> [2, 4, 6]
Group: Odd -> [7]
Group: Even -> [8, 10]
Group: Odd -> [11]
Group: Even -> [12]
Group: Odd -> [13]
Explanation: This example groups numbers into consecutive even and odd numbers. The groupby() function checks the parity of each number and forms groups accordingly. The output shows the even and odd groups.

2. Grouping Strings Based on Length
In this example, itertools.groupby() is used to group strings based on their length, categorizing words into groups of equal length.




import itertools

# List of strings
l = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

# Grouping strings by their length
g_data = itertools.groupby(l, key=lambda x: len(x))

# Display grouped elements
for key, group in g_data:
    print(f"Length: {key} -> {list(group)}")

Output
Length: 5 -> ['apple']
Length: 6 -> ['banana', 'cherry']
Length: 4 -> ['date']
Length: 3 -> ['fig']
Length: 5 -> ['grape']
Explanation: Here, words are grouped by their length using the groupby() function. It categorizes the words into groups of the same length, and the output displays these groups.

'''