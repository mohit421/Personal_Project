# Map and Filters that make use of the lambda func
# Map returns a map objects
x = [1,2,3,4,5,6,7,8,8,9,67,45,5465,5,23,45,45,35,54,546,56]

mp = map(lambda i:i*2,x)
print(list(mp))

# filter
# Instead of returning value it returns true or false
# It gonna tell us whether or not we should include the items 
# in our final filtered list objects

# only return if it is even
mp = filter(lambda i:i%2==0,x)
print(list(mp))

# other ways if instead of lambda if we use 

def func(i):
    i = i*3
    return i%2==0

mp = filter(func,x)
print(list(mp))