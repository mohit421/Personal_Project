def func():
    print('Run')
    def func():
        print("hi")
    func()

func()



def func(x,y):
    print('Run',x,y)
x,y = 5,4
func(x,y)


def func(x,y):
    print('Run',x,y)
    return x*y
x,y = 5,4
print(func(x,y))

# If we return mutliple things then we got our result in tuples

def func(x,y):
    print('Run',x,y)
    return x*y, x/y 

print(func(5,6))


def func(x,y):
    print('Run',x,y)
    return x*y, x/y 

r1, r2 = func(5,6)

print(r1,r2)

def func(x,y,z=None):
    print('Run',x,y,z)
    return x*y,x/y ,z

r1,r2,r3 = func(5,6,7)
print(r1,r2,r3)