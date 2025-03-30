# Python Object-Oriented Programming



# Why should even we use classes

# This is too specific to python
# Classes is used by most modern programming languages adn there is a good reason for that.

# This allows us to logically group our data and function and easy to reuse 
# and also easy to build upon if need be


# We we say data and function that are associated with specific classes twe
#  called those attribute and methods in class

# -----------------------------METHOD-----------------------
#  A function that associated with a class 


# --------------------------------- 
# We have a application for  a company and we want to represent our employees in python code 
# this should be a great usecase for a class cuz each individual employees have specific attributes and methods

# For examples:- Each employee have email address, name , a pay and also action that they can perform 
#  So be nice if we have class that we can use as a blueprint to create each employee , SO we don't have to do manually each time from scratch


#  Employee Class with no attribute and method
class Employees:
    pass

# -----------------------------------------------------------
# --------------- Difference b/w class and instances

# ---------------- CLASS - ------------------------------------------
# A class is basically a blueprint for creating instances and each unique employee 
# that we create using a Employee class will be an instance of that class 

class Employee:
    pass

# Instances
# Each of this going to be their own unique instances of the employee class
emp1_1 = Employee() 
emp1_2 = Employee() 

# both emp1_1 and emp1_2 are Employees Objects and both unique and both are at unique location in memory
print(emp1_1)
print(emp1_2)



# --------------INSTANCE VARIABLE -----------------------------------

'''
#
#  Instance variables contains data that is unique to each instance 

# We could manually create instance variable for each employee by doing something like below
'''


emp1_2.first = 'Mohit'
emp1_2.last = "Jaiswal"
emp1_2.email = "mohitjais312@gmail.com"
emp1_2.pay = 900000


emp1_1.first = 'Test'
emp1_1.last = "Scream"
emp1_1.email = "test@gmail.com"
emp1_1.pay = 1500000
# print(emp1_1.first + emp1_1.last)
# print(emp1_1.pay)
# print(emp1_1.email)
# print(emp1_2.first + emp1_1.last)
# print(emp1_2.pay)
# print(emp1_2.email)


'''
# Create instance variable rather than manually
# Bcuz we don't get much benifit of classes if we create instance variable manaully

#  To make he setup automatically when we create an employee
#  We use the special init methods, we can thing of this methods as initialized
# and if we coming from another language then we can things of this as constructor
'''



class EmployeeS:
    '''
        # Self is the instance, that means emp1_1.first = first is same as self.first = first
        # Instead of manually this is create automatically when we create our employee objects
        # This don't need to be same as our employee objects we can use fname instead first or anything
    '''
   
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

'''
# Now we have to pass the value that we initialized in our init method
# Init method takes the instance called as self and  first, last and pay 
'''

emp_1 = EmployeeS('Mohit', 'Jaiswal','900000')
emp_2 = EmployeeS('Test','Scream',150000)
# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)
