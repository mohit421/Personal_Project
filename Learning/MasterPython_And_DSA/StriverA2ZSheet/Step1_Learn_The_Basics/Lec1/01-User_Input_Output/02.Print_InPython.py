# Problem Link:- https://www.geeksforgeeks.org/problems/print-in-python/1&selectedLang=python3


# Solution 1

#User function Template for python3
a = input()
b = input()
separator = input()[0]

########### Write your code below ###############

# Print with space
print(a,b)

# Print without newline at the end
print(a,b,end='')
# Print with separator
print(a,b, sep = separator)

# Print without space
# print(a,b,sep='')
print(a+b)
########### Write your code above ###############