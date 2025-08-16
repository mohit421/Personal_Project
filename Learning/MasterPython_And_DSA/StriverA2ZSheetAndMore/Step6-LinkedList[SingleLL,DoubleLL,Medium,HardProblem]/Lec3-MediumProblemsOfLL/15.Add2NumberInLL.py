'''

'''

# Solution 1

'''

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2 = l1,l2
        dummyNode = ListNode(-1)
        curr = dummyNode
        carry = 0
        while t1 or t2:
            sum = carry
            if t1:
                sum += t1.val
            if t2:
                sum += t2.val
            newNode = ListNode(sum%10)
            carry = sum//10
            curr.next = newNode
            curr = curr.next
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        if carry:
            newNode = ListNode(carry)
            curr.next = newNode
        
        return dummyNode.next
    

    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum//10
            node = ListNode(sum%10)
            temp.next = node
            temp = temp.next
        return dummy.next
