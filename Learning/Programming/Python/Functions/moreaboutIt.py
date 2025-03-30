# Unpack operator / *args and **kwargs

# def func(x):
#     def func2():
#         print(x)
#     return func2 

# # below is equals to :- x = func(3) and then we call x()

# print(func(3)())



def func(*args, **kwargs):
    pass


x = [1,23,23432,23423]
# *x this will unpack all the x out and separate them buy 
# individual element and pass them to print statement
print(x)
print(*x)

def func2(x,y):
    print(x,y)

pairs = [(1,2),(3,4)]

for pair in pairs:
    # This is not the pythonic way to do this
    # func2(pair[0],pair[1])
    # below *pair will unpack them and pass it to func2 as
    #  func2(1,2) and func2(3,4)
    func2(*pair)


def func3(x,y):
    print(x,y)


# func3(**{'x':2,'y':5})
# if x and y is not in correct order then also this will work
func3(**{'y':8,'x':7})


# *args and **kwargs :-
#  Imagine we have a function and we don't know how many arguments, positional or keyward arguments we want to accept 
#  kwargs stands for keyword arguments
# it will allows to pass an unlimited amount of regular arguments and keyword arguments.
# So, if I actually go funk, and then I pass like 1,2,3,4,5 and may be pass an keyword arguments 
# like one= 0,  two=1
# When we printed args and kwargs we are gettings a tuple that has all of the positional arguments which are 1,2,3,4,5 
# and all of the  keyword arguments which are one  and two
# if i want to use any of these then we can unpack them 

# def func(*args, **kwargs):
#     print(args, kwargs)

# func(1,2,3,4,5,one=0,two=1)


# # We can unpack args like *args
# def func(*args, **kwargs):
#     print(*args)

# func(1,2,3,4,5,one=0,two=1)


# We can unpack kwargs like **kwargs
def func4(*args, **kwargs):
    # What below print will do  **kwargs is it will be treated 
    # like print(one=0 , two=1) , so this are not valid argument for print statement so we are getting error

    print(dict(**kwargs))

func4(1,2,3,4,5,one=0,two=1)

