# Removing duplicates from a list while applying a function

nums = [1,2,2,3,3,3,4,4,4,4]

unique_squares = {x**2 for x in nums}
# print(unique_squares)


# Set Comprehension

nums = [1,1,2,1,3,4,5,5,6,7,8,7,9,9]

my_set = set()
for n in nums:
    my_set.add(n)
# print(my_set)

# Using Set Comprehension
my_set = {n for n in nums}
# print(my_set)


