# Problem:- https://www.geeksforgeeks.org/problems/the-dice-problem2316/1?&selectedLang=python3?

'''
For a standard die:

Opposite pairs are:

1 ⟷ 6

2 ⟷ 5

3 ⟷ 4
So, the opposite of any face n is 7 - n
'''

def opposite_face(n):
    if 1 <= n <= 6:
        return 7 - n
    else:
        raise ValueError("Input must be between 1 and 6 inclusive.")


# Solution

class Solution:
    def oppositeFaceOfDice(self, n):
    	#code here 
    	return 7-n
