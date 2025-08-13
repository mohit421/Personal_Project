'''

'''

# Brute force

'''
Complexity Analysis

Time Complexity: O(N) + O(N log N) + O(N)where N is the number of nodes in the linked list.

O(N) to traverse the linked list and store its data values in an additional array.
O(N log N) to sort the array containing the node values.
O(N) to traverse the sorted array and convert it into a new linked list.
Space Complexity : O(N)where N is the number of nodes in the linked list as we have to store the values of all nodes in the linked list in an additional array to sort them.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        temp = head
        arr.sort()
        for i in range(len(arr)):
            temp.val = arr[i]
            temp = temp.next
        
        return head


# Optimised Approach using Merge Soret concept

'''
Complexity Analysis

Time Complexity: O(N log N)where N is the number of nodes in the linked list. Finding the middle node of the linked list requires traversing it linearly taking O(N) time complexity and to reach the individual nodes of the list, it has to be split log N times (continuously halve the list until we have individual elements).

Space Complexity : O(1) as no additional data structures or space is allocated for storage during the merging process. However, space proportional to O(log N) stack space is required for the recursive calls. THe maximum recursion depth of log N height is occupied on the call stack.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoSortedLinkedList(self, left: Optional[ListNode], right: Optional[ListNode])-> Optional[ListNode]:
        dummyNode = ListNode(-1)
        temp = dummyNode
        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        
        if left:
            temp.next = left
        else:
            temp.next = right
        return dummyNode.next



    def findMidEle(self, head: Optional[ListNode])-> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        midEle = self.findMidEle(head)
        right = midEle.next
        midEle.next = None
        left = head
        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeTwoSortedLinkedList(left,right)
