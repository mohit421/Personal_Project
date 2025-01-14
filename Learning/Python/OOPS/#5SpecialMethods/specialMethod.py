# `````````````````````````````````SPECIAL METHOD ````````````````````===============
# ---------------------------------  SPEICAL (MAGIC/DUNDER) METHOD


class Employee:
    # class variable
    num_of_emps = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        Employee.num_of_emps +=1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):        
        self.pay = int(int(self.pay) * self.raise_amt)


emp_1 = Employee('Mohit', 'Jaiswal',900000)
emp_2 = Employee('Test','Scream',150000)

'''
Behaviour of adding two string together is totally different from adding two integer together
Strings get concatenate and integers get added
Depending of whats objects we are working with the addition actually has different behaviour

'''
print(1+2)
print('a'+'b')


'''

If we want to print out employee instance then we can see that we just get the vague employee object and it
 would be nice if we could change this Behavior to print out something a little bit more userfriendly
 that's what these special methods are going to allow us to do 
 - By definding own buildin methods we'll be able to change some of this built-in behavior and operations
 - These special methods are alwys surrounded by double underscores 
 - Lots of people called this double underscore Dunder 
 - If someway say dunder init then that measn __init__ ( ie.,init surrounded by double underscore)
 - Dunder init is the first and most common that everyone using it
 - Special dunder init method is called when we create our employee objects
 - and it comes in and sets all of our attribute for us 
 

'''
print(emp_1)




# ------------------------------------------Some other common special methods --------------------

'''
Two common meehods that we should probably always implement are :-

1. __repr__(self):- 
    - It meant to be an unambiguous reprentation of the object and should be used for debugging and logging the things like that 
    - It really meant to be seen by other developers
    - 
2. __str__(self):- 
    - It meant to be more of readable representtation of an object and is meant to be used as a display to the end user 
    - 
'''


class Employee:
    # class variable
    num_of_emps = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        Employee.num_of_emps +=1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):        
        self.pay = int(int(self.pay) * self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)


emp_1 = Employee('Mohit', 'Jaiswal',900000)
emp_2 = Employee('Test','Scream',150000)

# print(emp_1)
# repr(emp_1)
# str(emp_1)
'''
These two special methods allow us to change how our object are printed and  displayed now to be honest 
unless we're writing some complicated classes  __init__ , __repr__ and __str__ are most used  

'''
# print(emp_1.__repr__())
# print(emp_1.__str__())



# --------------------------------

# print(1+2)
'''
# What above line of do behind the scene is below 
#  using our own dunder method __add__()
'''

# print(int.__add__(1,2))


# -------------------- CODE
'''
We want to display total salary so we can do thsi by adding two employee salary using __add__()



'''

class EmployeeS:
    # class variable
    num_of_emps = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        EmployeeS.num_of_emps +=1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):        
        self.pay = int(int(self.pay) * self.raise_amt)

    def __repr__(self):
        return "EmployeeS('{}','{}',{})".format(self.first,self.last,self.pay)
    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)
    '''
    If we don't have below dunder add emthod then we will get error 

    '''
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())

emp_1 = EmployeeS('Mohit', 'Jaiswal',900000)
emp_2 = EmployeeS('Test','Scream',150000)

print(emp_1 + emp_2)


'''
There are more special methods are there we can check python docs for that 

'''
print(len(emp_1))
print(len('test'))
# This also using special dunder method behind the scence
print('test'.__len__())