# It is unordered unique collection of elements
# What that means? 
#  there is no duplicate elements
#  we don't keep track of order or frequency of the element
# Set is extremely fast to do with lookups and removals or additions



y = set()
s = {4,32,2,2}
print(type({}))
print(s)

s.add(5)
print(s)

s.remove(2)
print(s)

print(46 in s)


s1 = [4,32,2,2]

print(32 in s1)


s2 = {3,2,22,1}
print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))
