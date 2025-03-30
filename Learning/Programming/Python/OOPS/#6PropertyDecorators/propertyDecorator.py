
# --------------------------   Property Decorators- Getters, Setters, and Deleters ----------------------------


'''
If we change the first then we don't have problem with full name but what is with email it will not updated
Problem here is with email
Let say people don't want to change the email everytime they change their first name. they want to update the email automatically

- Everyone's first thought is to create a email method just like full name
- the problem with that is it will break the code everyone currently using the class 
- so they have to go through and change every instance of the email attribute with an email method now this 
- this is usually where people from other languages like Java will bring up the benefits of getter and setter methods
- This is very good point where getter and setter really come in handy but we have the ability to do this within python
- using the property decorator , Property decorator allows us to define a method but we can access it like an attribute
- so for example let's go ahead and pull this email attribute out into a method similar to our fullname method so
- so this solved our problem where it set our email address to new first name but this also means that
 anyone using our class would have to change their code also take the parentehsis off from email() as shown in next example code
- 
'''
class Employee:

    def __init__(self, first, last):
        # instance variable
        self.first = first
        self.last = last

    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    


emp_1 = Employee('Mohit', 'Jaiswal')

emp_1.first = 'Jimmy'
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.fullname())
# print(emp_1.email())




# ``````````````````````````````````````````````````````CODE------------------------


class EmployeeS:

    def __init__(self, first, last):
        # instance variable
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
'''
 For this take the parenthesis off parenthesis and add @property above email method
 - Just by making this small change now if we run our code then we can see that works 
 - We're defining our email in our class like it's a method but we're able to access it like an attribute
 and we can do this just as easily with fullname as well 
'''

emp_1 = EmployeeS('Mohit', 'Jaiswal')

emp_1.first = 'Jimmy'
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.fullname())
# For this take the parenthesis off parenthesis
# print(emp_1.email)



# --------------------------------------------------CODE ---------------------------------



class EmployeeST:

    def __init__(self, first, last):
        # instance variable
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_S = EmployeeST('Mohit', 'Jaiswal')

# emp_S.first = 'Jimmy'
# print(emp_S.first)
# print(emp_S.last)
# print(emp_S.fullname)
# For this take the parenthesis off parenthesis
# print(emp_S.email)



# ----------------------------------------------- Setter --------------------------------

'''
We want that by setting full name we want to change in our first name , last name and email as well 
Right now we can't do that
- IF we only have fullname with the property decorator and I try to set this like this then we will get error 
- AttributeError: property 'fullname' of 'EmployeeSTR' object has no setter
- So for doing this we need to use setter and that going to be another decorator now

'''

class EmployeeSTR:

    def __init__(self, first, last):
        # instance variable
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1STR = EmployeeSTR('Mohit', 'Jaiswal')


# emp_1STR.fullname = 'Corey Schafer'


emp_1STR.first = 'Jimmy'
# print(emp_1STR.first)
# print(emp_1STR.last)
# print(emp_1STR.fullname)
# print(emp_1STR.email)




# ------------------------------------------ CODE Setter =----------------------------



class Employee1:

    def __init__(self, first, last):
        # instance variable
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_11 = Employee1('Mohit', 'Jaiswal')


emp_11.fullname = 'Corey Schafer'
# print(emp_11.first)
# print(emp_11.last)
# print(emp_11.fullname)
# print(emp_11.email)



#`````````````````````````````````````````````` CODE DELETER `````````````````````````````````````````````

'''
We can also make the deleters in the same way like setter
- Let say that if i want to delete the full name of employee that I wanted to run some kind of cleanup
- Code to do this look below code
'''


class Employee1:

    def __init__(self, first, last):
        # instance variable
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_12 = Employee1('Mohit', 'Jaiswal')


emp_12.fullname = 'Corey Schafer'


print(emp_12.first)
print(emp_12.last)
print(emp_12.fullname)
print(emp_12.email)

del emp_12.fullname


print(emp_12.first)
print(emp_12.last)
print(emp_12.fullname)
print(emp_12.email)