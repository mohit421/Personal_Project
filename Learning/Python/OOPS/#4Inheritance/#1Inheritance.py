# ------------------------------------------------ INHERITANCE ------------------------------------

'''
Inheritance:-
- It allow us to inherit the methods and attributes from parent class 
- This is useful bcuz we can create sub-classes and get all of the functionality of our parent class
- we can override or add new functionality without affecting the parent class in anyway

'''

# -------------- EXAMPLEs-----------------------

'''
- Let say we want to create specific types of Employees 
- let say Developers and Managers - this will be good candidates for subclasses
- Both developer and managers have name, email address and salary those all are in employee class already has
- So instead of copying all these code into managers and developers subclasses we reuse that code by inheriting 
from Employee
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

'''
By inheriting the Employee class into developer subclass - that's inherit all of its functionality

'''
class Developer(Employee):
    pass

dev_1 = Developer('Mohit', 'Jaiswal',900000)
dev_2 = Developer('Test','Scream',150000)

# print(dev_1.email)
# print(dev_2.email)

'''
Below help() function will print all kind of good information abou this like forr developer from below print

'''
# print(help(Developer))



# ----------------------------------------------------


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


class Developer(Employee):
    pass

dev_1 = Developer('Mohit', 'Jaiswal',900000)
dev_2 = Developer('Test','Scream',150000)
# print(dev_1.pay)
dev_1.apply_raise()
# print(dev_1.pay)




# ----------------------------------------------------

'''
# Let say our developer have raise_amt of 1-% 
'''


class Employee1:
    # class variable
    num_of_emps = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        Employee1.num_of_emps +=1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):        
        self.pay = int(int(self.pay) * self.raise_amt)


class Developer1(Employee1):
    raise_amt = 1.10

dev_1 = Employee1('Mohit', 'Jaiswal',900000)
'''
# below changes doesn't impact anything in parent class 
'''
# dev_1 = Developer1('Mohit', 'Jaiswal',900000)
dev_2 = Developer1('Test','Scream',150000)
# print(dev_1.pay)
dev_1.apply_raise()
# print(dev_1.pay)




# ````````````````````````````````````````` More Complex Chnages in Developer Class -----------------------




class Employee2:
    # class variable
    num_of_emps = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        Employee2.num_of_emps +=1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):        
        self.pay = int(int(self.pay) * self.raise_amt)


class Developer2(Employee2):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        '''
        Below both the way calling the init method will work
        but use super() 
        bcuz single inheritance like we are using below it's a little bit more 
        maiintainable 
        Always stick with super()
        super().__init__( first, last, pay)
        not below way
        # Employee.__init__(self, first,last,pay)
        '''
        super().__init__( first, last, pay)
        # Employee2.__init__(self, first,last,pay)
        self.prog_lang = prog_lang


'''
Now, When we instantiate our developers down here it's also going to be expecting programming language 
here which to be passed in 
'''

dev_12 = Developer2('Mohit', 'Jaiswal',900000,'Python')
dev_22 = Developer2('Test','Scream',150000, 'C++')


# print(dev_12.email)
# print(dev_12.prog_lang)
# print(dev_22.email)
# print(dev_22.prog_lang)





# -----------------------------Another subclass manager ---------------------------


class Employee3:
    # class variable
    num_of_emps = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        Employee3.num_of_emps +=1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):        
        self.pay = int(int(self.pay) * self.raise_amt)


class Developer3(Employee3):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__( first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employeeslist=None):
        super().__init__( first, last, pay)
        if employeeslist is None:
            self.employeelists = []
        else:
            self.employeeslist = employeeslist
    
    def add_emp(self, emp):
        if emp not in self.employeeslist:
            self.employeeslist.append(emp)
    def remove_emp(self, emp):
        if emp in self.employeeslist:
            self.employeeslist.remove(emp)
    def print_emp(self):
        for emp in self.employeeslist:
            print('-->', emp.fullname())

dev_13 = Developer3('Mohit', 'Jaiswal',900000,'Python')
dev_23 = Developer3('Test','Scream',150000, 'C++')


mgr_1 = Manager('Sue', 'Smith', 40000, [dev_1])


# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emp()



# ``````````````````````````````BUILTIN FUNCTION --------------------

'''
ininstance():- 
issubclass()
'''
# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Developer))

# print(issubclass(Manager, Developer))
# print(issubclass(Developer, Manager))


