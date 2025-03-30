# ------------------------ METHOD --------------------------------------------

# We want the ability to perform some kind of action now to do that we can add
#  some Method to our class 

# Let's say we want the ability to display the full name of an employee 
#  this is the action we likely need to do a lot like this so 
# we can do this manually outside the class 

class EmployeeS:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

emp_1 = EmployeeS('Mohit', 'Jaiswal','900000')
emp_2 = EmployeeS('Test','Scream',150000)
# print(emp_1.email)
# print(emp_2.email)

# This a lot of type in each time we want to display the employees full name
#  So instead we can create a method inside of our class to put this functionality in one place

# print('{} {}'.format(emp_1.first,emp_1.last))


# --------------------------------------------------------------_________+++++++++++++++



class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
    # Each method within a class automatically take instance as the first argument
    #  and we always called as  Self and instance is the only argument that are needed to
    #  get our full name 
    # 

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee('Mohit', 'Jaiswal','900000')
# emp_2 = Employee('Test','Scream',150000)
# print(emp_1.email)
# print(emp_2.email)

# This a lot of type in each time we want to display the employees full name
#  So instead we can create a method inside of our class to put this functionality in one place

# print('{} {}'.format(emp_1.first,emp_1.last))
# print(emp_1.fullname())

#  Now we have full advantage of code resue here 
# print(emp_2.fullname())

# below will return method instead of return value of method
# print(emp_2.fullname)


# One common methods that we see while creating an method is forgetting the self argument
#  how it will look like when we off self argument inside m ethod



"""

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    def fullname():
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee('Mohit', 'Jaiswal','900000')
emp_2 = Employee('Test','Scream',150000)
# this will run without any errors 

#  but we if we try to this method fullname() we accidentally left of with typeerror
# TypeError: Employee.fullname() takes 0 positional arguments but 1 was given
# Below is doesn't like we have passed in any argument below but the instance 
# in this case emp_1 is passed automatically so we expect instance argument in our methods
# that's why we add self 
print(emp_1.fullname())

"""




# ______-----------------------------------------



class EmployeeT:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = EmployeeT('Mohit', 'Jaiswal','900000')
emp_2 = EmployeeT('Test','Scream',150000)


# We can run this method with the class name itself
# This is just make a bit more obvious is what going on in the background 
# We manually pass in the instance as argument
print(EmployeeT.fullname(emp_1))
# both below and above line do the same thing 
print(emp_1.fullname())


