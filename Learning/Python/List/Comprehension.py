

x = [x for x in range(5)]
print(x)


x = [x+6 for x in range(5)]
print(x)


x = [x%2 for x in range(5)]
print(x)



# x = [[0 for x in range(100)] for x in range(5)]
# print(x)


x = [i for i in range(100) if i%5 ==0]
print(x)


# Dict

x = {i:0 for i in range(100) if i%5 ==0}
print(x)

# Sets
x = {i for i in range(100) if i%5 ==0}
print(x)


x = tuple(i for i in range(100) if i%5 ==0)
print(x)
