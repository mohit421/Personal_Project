# List
# 1. It is an ordered Collection
# 2. List it mutable. this can be changed

x = [4,True,'Hi']
y = 'hi'
# print(x,len(x),len(y))

# It ends to the end of the list
x.append('Hello')
# print(x)

# x.append([4,5,6,3,23,23,4,5])
# print(x)


# We can extends the list by another list by appending each of those in the another list

x.extend([4,5,6,3,23,23,4,5])
# print(x)




# Removing something from the list

x.pop()
# print(x)

x.pop(0)
# print(x)

# print(x[1])
y = x

# Made in modification in x that made in modification in y because y is reference to the list not copy of the list
x[0] = 'mohit'
# print(x)

print(x,y)


# Copy the list 

z = x[:]

x[1] ='mi'
print(x,z)