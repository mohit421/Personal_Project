'''

'''


# Solution
'''

'''


# Using three variable

class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        # code here
        temp = a
        a = b
        b = a
        return (a,b)

# Using two variable
'''
a = a^b
b = a^b = (a^b)^& = a
a = (a^b)^b = = a^b^a = b

'''
class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        # code here
        a = a^b
        b = a^b
        a = a^b
        return (a,b)