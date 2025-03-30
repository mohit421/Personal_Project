# `````````````````````````````````CLASS METHOD -----------------------------------


#-------------------------- DIFFERENC WITH REGULAR METHOD, CLASS METHOD AND STATIC METHODS ----------------



'''
# **Regular Method**:-
- Regular Method in a class automatically takes the insance as the first argument and by 
convenction we are calling this as self 

# How can we change this so that it instead automatically take the class as the first argument?
### So to do this we use class Method

### To turn a **Regular method** into a **class method** 
- it is easy as decorators on the top called @classmethod

# By convection as a regular method we called class as **self**
and for **class mthiod** we called as **cls**

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
    
    @classmethod
    def set_raise_amt(cls,amount):
        pass

# print(EmployesSTRF.num_of_emps)
emp_1 = EmployesSTRF('Mohit', 'Jaiswal','900000')
emp_2 = EmployesSTRF('Test','Scream',150000)
# emp_2 = EmployesSTRF('Test','Scream',150000)
# print(EmployesSTRF.num_of_emps)



'''


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


emp_1 = Employee('Mohit', 'Jaiswal',900000)
emp_2 = Employee('Test','Scream',150000)



# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)


'''
# nopw we are working with class instead of instances
# We are using class method to set raise amt for changing raise-amt

'''
Employee.set_raise_amt(1.05)
# Below is just similar to above line
# Employee.raise_amt = 1.05

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)



# ------------------------------------
''''
- Use classmethod as alternative constructor 
# Q) What does above line means?
- we can use this class method in order to provide mutliple ways for creating our objects 
- Let say for example someone is using our ** Employee class ** ans they say hey 
- I have specific usecases where I am getting employee information in the form of string separated by hyper(-)
- and I constantly needing to parse the string before I create new employees
- Is there a way to pass the string and create a employee from that 
'''

# ///////////////---------------- Common USecase example ------------------

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


emp_1 = Employee('Mohit', 'Jaiswal',900000)
emp_2 = Employee('Test','Scream',150000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-60000'
emp_str_2 = 'Virat-Kholi-90000'

'''
If we wanted to create a new employee from the string then first we have to do split the string 
but using bewlow way is not he usecase to split everything we need to prase the string 
# Buit if this is the common usecase to do so we can't do like below 
#  Lets just create alternative constructor check another below example for that
'''
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first,last,pay)
# print(new_emp_1.email) 
# print(new_emp_1.pay) 


# ///////////////---------------- Common USecase example Alternative constructor ------------------

# We can use class method as alternative constructor belwo is the example usecase for that
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


emp_1 = Employee('Mohit', 'Jaiswal',900000)
emp_2 = Employee('Test','Scream',150000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-60000'
emp_str_2 = 'Virat-Kholi-90000'


new_emp_1 = Employee.from_string(emp_str_1)
new_emp_1 = Employee.from_string(emp_str_2)

# print(new_emp_1.email)
# print(new_emp_1.pay)



# ------------------------------------Real world example or above---------------------------------


from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def from_FathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def from_BirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Female'

man = Man.from_BirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.from_FathersAge('John', 1965, 20)
print(isinstance(man1, Man))
