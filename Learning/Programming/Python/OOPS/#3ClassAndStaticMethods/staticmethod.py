# ----------------------------------- STATIC METHOD -----------------------------------


'''
- Regular method pass the self as the first argument
- Class method pas the cls as the first argument

# Static Method
- static method don't pass anything automatically they don't pass the insance(self) or the class (cls)
- This behave just like regular function except we don't include this in our class cuz we have some logical connection
with class

- 

'''

'''
Let say we wanted a simple function that would taken a date and return whether or not that was a work day
 so that has the logical connection to our employee class but it doesn't depend on specific instances or class variable
 instead we make that a static method

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
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee('Mohit', 'Jaiswal',900000)
emp_2 = Employee('Test','Scream',150000)

import datetime
# my_date = datetime.date(2016,7,10)
my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))

'''
If we doesn't use a cls in class methiod or self in regular method 
then we need to that check that whether or not we need to se a static method 

'''