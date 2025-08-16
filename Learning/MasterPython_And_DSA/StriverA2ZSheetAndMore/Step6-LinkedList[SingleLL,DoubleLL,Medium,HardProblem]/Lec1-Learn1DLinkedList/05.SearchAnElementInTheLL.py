'''
https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1
'''


#User function Template for python3


''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchKey(self, n, head, key):
        #Code here
        curr = head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
            
        return False