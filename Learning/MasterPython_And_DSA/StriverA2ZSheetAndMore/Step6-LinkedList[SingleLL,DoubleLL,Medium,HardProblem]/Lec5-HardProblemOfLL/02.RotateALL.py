'''

'''
# Brute force solution
'''
Time Complexity: O(Number of nodes present in the list*k)

Reason: For k times, we are iterating through the entire list to get the last element and move it to first.

Space Complexity: O(1)

Reason: No extra data structures is used for computations
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None: return head

        for i in range(k):
            temp = head
            while temp.next.next:
                temp = temp.next
            lastNode = temp.next
            temp.next = None
            lastNode.next = head
            head = lastNode
        return head



# Optimal Solution
'''
Time Complexity: O(length of list) + O(length of list - (length of list%k))

Reason: O(length of the list) for calculating the length of the list. O(length of the list - (length of list%k)) for breaking link.

Space Complexity: O(1)

Reason: No extra data structure is used for computation.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findNthNode(self, head : Optional[ListNode], n:int)-> Optional[ListNode]:
        cnt = 1
        temp = head
        while temp:
            if cnt == n:
                return temp
            cnt += 1
            temp = temp.next
        return temp

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head== None or k == 0: return head
        len = 1
        tail = head
        while tail.next:
            len += 1
            tail = tail.next
        if k%len ==0:
            return head
        k= k%len
        tail.next = head
        newLastNode = self.findNthNode(head,len-k)
        head = newLastNode.next
        newLastNode.next = None
        return head
