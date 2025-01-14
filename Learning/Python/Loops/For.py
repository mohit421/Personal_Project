# Allows us to iterate sets number of times

# for i in range(10):
#     print(i)

# start, stop and step
# stop :- usually range start with zero. by default our range start at zero and go the the 10-1 if use range(10)

# start, stop :- range(1,10) :- by default we start by 1 and and stop at 10 print from 1 to 9 but not include 10

#  start, stop, step :- range(1,10,3):- we increment 3 every single time
# range(x,y,z) :- start from x and stop at y and step z each time

# for i in range (10,-1,-1):
#     print(i)


# for i in [3,4,5,2,1,4,5]:
#     print(i)

x = [2,3,4,5,5,3]
# for i in range (len(x)):
#     print(i)


for i, ele in enumerate(x):
    print(i, ele)