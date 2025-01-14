#   ````````````````````````````CLASS VARIABLE--------------------------



# ``````````````````````````````````CODE ------------------------
class EmployeeS:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

emp_1 = EmployeeS('Mohit', 'Jaiswal','900000')
emp_2 = EmployeeS('Test','Scream',150000)


print(emp_1.email)
print(emp_2.email)

'''
                                Instance varibale:-
Which are used to data that are unique to each instance
WE Saw a first, last and pay in ou init method those are set for each instances of the employee
that we create  


'''
'''
                                CLASS VARIABLE:-
This are varibale that are shared among all instances of the class  
so while instance variable can be unique for each instance like our name ,. email and pay 
Class variable should be the same for each instance
'''


# ``````````````````````````````````CODE ------------------------
'''
What kind of data should eb shared among all employees ?
- A lots of ideas we can comes up with but for below example
- lets say our company gives annual rages every year
- now the amount can change from year to year
- whatever the amount it should be same for all employees that can be a 
god candidate for a class variable

'''
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(int(self.pay) * 1.40)

emp_1 = Employee('Mohit', 'Jaiswal','900000')
emp_2 = Employee('Test','Scream',150000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)



# --------------------------------------CODE --------------

class EmployesST:
    # class variable
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        # instead of using hard coded we can use class variable
        self.pay = int(int(self.pay) * int(EmployeeS.raise_amount))
        # if this a class variable how below can print it using instance variable
        # self.pay = int(int(self.pay) * self.raise_amount)

emp_1 = EmployesST('Mohit', 'Jaiswal','900000')
emp_2 = EmployesST('Test','Scream',150000)

# we can access class vaiable using both instances and class as well

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(EmployesST.raise_amount)



# --------------------------------------CODE --------------

class EmployesSTR:
    # class variable
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        # instead of using hard coded we can use class variable
        self.pay = int(int(self.pay) * int(EmployeeS.raise_amount))
        '''
        # if this a class variable how below can print it using instance variable
        # using self with raise_amount this gives us ability to change that amount for a single instances 
        # if we really wanted to change emp_1 raise amount than we can do and if we apply_raise then  it will use emp_1 raise_amount
        # instead of classes raise_amount

        # also using self here it allows any sub-class  to override that constant if they wanted to
        '''
        
        # self.pay = int(int(self.pay) * self.raise_amount)

emp_1 = EmployesSTR('Mohit', 'Jaiswal','900000')
emp_2 = EmployesSTR('Test','Scream',150000)

# print namespace of emp_1
# output :- {'first': 'Mohit', 'last': 'Jaiswal', 'pay': '900000', 'email': 'Mohit.Jaiswal@company.com'} 
# print(emp_1.__dict__)


'''
# Ouput :- {'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function EmployesSTR.__init__ 
# at 0x00000276BF54A160>, 'fullname': <function EmployesSTR.fullname at 0x00000276BF54A200>, 'apply_raise': 
# <function EmployesSTR.apply_raise at 0x00000276BF54A2A0>, '__dict__': <attribute '__dict__' of 'EmployesSTR' objects>,
#  '__weakref__': <attribute '__weakref__' of 'EmployesSTR' objects>, '__doc__': None}
'''

# print(EmployesSTR.__dict__)


# EmployesSTR.raise_amount = 1.05
# print(EmployesSTR.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# Instead of doing change in raise_amount by class name use instances 
emp_1.raise_amount = 1.05 # this will only change raise-ampunt for emp-1

# print(EmployesSTR.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

'''
#  Now we can see emp_1 has raise_amount in its namespace eaqual to 5% , and its find its own namespace so it print by checking its namespace instead searching for class vareiabale
# we didn't set for emp_2 so that looks for class variable value
'''

print(emp_1.__dict__)




# --------------------------------------------Another example of classs varaible --------------------------

'''

'''


class EmployesSTRF:
    # class variable
    num_of_emps = 0
    raise_amount = 1.04


    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        EmployesSTRF.num_of_emps +=1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):        
        self.pay = int(int(self.pay) * self.raise_amount)

print(EmployesSTRF.num_of_emps)
emp_1 = EmployesSTRF('Mohit', 'Jaiswal','900000')
emp_2 = EmployesSTRF('Test','Scream',150000)
# emp_2 = EmployesSTRF('Test','Scream',150000)
print(EmployesSTRF.num_of_emps)