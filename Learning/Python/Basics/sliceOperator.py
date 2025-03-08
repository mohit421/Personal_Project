x = [0,1,2,3,4,5,6,7,8]
y = ['hi','hello','goodbye','cya','sure']

s = "hello"

# sliced = [start:stop:step]
# x[2:] :- start at 2 and stop at the end
# x[:0] :-  stop at 0 or whatever at index 0
# x[2:4:] : statt at 2 , stop at 4 step by 1
# x[p4:2:-1] :- start at 4 and stop at 2 and step by -1
# x[::-1]: reverse a list in python

# x[::2] :- start at the beginning , stop at the end and step by 2
# This all worked in tuples as well

sliced = x[0:10:2]


print(sliced)


slice1 = (1,2,3,4,5,6,7,8)[::-2]
slice2 = (1,2,3,4,5,6,7,8)[::2]
print(slice1, slice2)