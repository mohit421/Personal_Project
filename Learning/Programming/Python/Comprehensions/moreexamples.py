# Code 1

nums = [1,2,3,4,5,6,7,8,9,10]

# I wan 'n for each 'n in nums
my_list = []
for n in nums:
    my_list.append(n)
# print(my_list)

# List comprehension of above code 1

my_list = [n for n in nums]
# print(my_list)

# ---------------------------------
# Code 2

# I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
# print(my_list)

# List Comprehension

my_list = [n*n for n in nums]
# print(my_list)

# Using a map and lambda

my_list = map(lambda n: n*n, nums)
# print(list(my_list))

# -------------------------------------------

# Code 3

# I wan 'n' for each 'n' to nums if 'n' is even

my_list = []
for n in nums:
    if n%2==0:
        my_list.append(n)
# print(my_list)

# List comprehension of above
my_list = [n for n in nums if n%2==0]
# print(my_list)

# Using filter and lambda function
my_list = filter(lambda n:n%2==0,nums)
# print(list(my_list))



# Code 4
# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'

my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
# print(my_list)

# Above code 4 into list comprehension

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)


