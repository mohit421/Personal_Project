'''
Find pairs with given sum in DLL
'''

# Brute force approach

from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""
'''
TC:- O(N^2)
SC:- O(N) in wrost case
'''
class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        temp1 = head
        lst = []
        while temp1:
            temp2 = temp1.next
            while temp2 and temp1.data + temp2.data <= target:
                if temp1.data + temp2.data == target:
                    lst.append((temp1.data,temp2.data)) 
                temp2 = temp2.next
            temp1 = temp1.next
        return lst
        

# Optimised solution using two pointer solution like we did in array 
'''
TC:- O(N)
SC:- O(N)
'''

from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        right = head
        while right.next:
            right = right.next
        
        left = head
        lst  = []
        while left.data < right.data:
            if left.data + right.data == target:
                lst.append((left.data,right.data))
                left = left.next
                right = right.prev
            elif left.data + right.data>target:
                right = right.prev
            else:
                left = left.next
        return lst