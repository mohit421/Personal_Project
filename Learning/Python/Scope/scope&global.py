# Scope and Global

x = 'Mohit'
def func(name):
    global x 
    x = name
    print(x)

print(x)
func('changed')
print(x)