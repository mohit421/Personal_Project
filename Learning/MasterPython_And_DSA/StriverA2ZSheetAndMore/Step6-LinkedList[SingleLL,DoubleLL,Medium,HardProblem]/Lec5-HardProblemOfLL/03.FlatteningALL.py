'''

'''


# Brute force Solution


'''
Complexity Analysis

Time Complexity: O(N*M) + O(N*M log(N*M)) + O(N*M)where N is the length of the linked list along the next pointer and M is the length of the linked list along the child pointer.

O(N*M) as we traverse through all the elements, iterating through ‘N’ nodes along the next pointer and ‘M’ nodes along the child pointer.
O(N*M log(N*M)) as we sort the array containing N*M (total) elements.
O(N*M) as we reconstruct the linked list from the sorted array by iterating over the N*M elements of the array.
Space Complexity : O(N*M) + O(N*M)where N is the length of the linked list along the next pointer and M is the length of the linked list along the child pointer.

O(N*M) for storing all the elements in an additional array for sorting.
O(N*M) to reconstruct the linked list from the array after sorting
'''

'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    
    def convertArrToLL(self, arr):
        dummy = Node(-1)
        temp = dummy
        
        for val in arr:
            temp.bottom = Node(val)
            temp = temp.bottom
        return dummy.bottom
            
    def flatten(self, root):
        #Your code here
        lst = []
        
        while root:
            
            temp1 = root
            while temp1:
                lst.append(temp1.data)
                temp1 = temp1.bottom
            root = root.next
            
        lst.sort()
        
        return self.convertArrToLL(lst)
    

# Optimal Solution 

'''
Complexity Analysis

Time Complexity: O( N*(2M) ) ~ O(2 N*M)where N is the length of the linked list along the next pointer and M is the length of the linked list along the child pointers.

The merge operation in each recursive call takes time complexity proportional to the length of the linked lists being merged as they have to iterate over the entire lists. Since the vertical depth of the linked lists is assume to be M, the time complexity for a single merge operation is proportional to O(2*M).
This operation operation is performed N number of times (to each and every node along the next pointer list) hence the resultant time complexity becomes: O(N* 2M).
Space Complexity : O(1) as this algorithm uses no external space or additional data structures to store values. But a recursive stack uses O(N) space to build the recursive calls for each node along the next pointer list.
'''

'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    
    def mergeTwoList(self, list1, list2):
        dummyNode = Node(-1)
        temp = dummyNode
        
        while list1 and list2:
            if list1.data < list2.data:
                temp.bottom = list1
                list1 = list1.bottom
            else:
                temp.bottom = list2
                list2 = list2.bottom
            temp = temp.bottom   # move temp downwards
        
        if list1:
            temp.bottom = list1
        else:
            temp.bottom = list2
        
        return dummyNode.bottom
            
            
            
    def flatten(self, root):
        #Your code here
        if not root or not root.next:
            return root
        mergeHead = self.flatten(root.next)
        root = self.mergeTwoList(root, mergeHead)
        return root
        