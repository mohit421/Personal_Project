'''

'''


# Brute force approach
'''
Time Complexity: O(m*n)

Reason: For each node in list 2 entire list 1 is iterated. 

Space Complexity: O(1)

Reason: No extra space is used.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headB is not None:
            temp = headA
            while temp is not None:
                if temp == headB:
                    return headB
                temp = temp.next
            headB = headB.next
        return None
    



# Optimised Approach used hashing


'''
Time Complexity: O(n+m)

Reason: Iterating through list 1 first takes O(n), then iterating through list 2 takes O(m). 

Space Complexity: O(n)

Reason: Storing list 1 node addresses in unordered_set.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        st =  set()
        while headA:
            st.add(headA)
            headA = headA.next
        while headB:
            if headB in st:
                return headB
            headB = headB.next
        return headB



# More optimised one
'''
Time Complexity:

O(2max(length of list1,length of list2))+O(abs(length of list1-length of list2))+O(min(length of list1,length of list2))

Reason: Finding the length of both lists takes max(length of list1, length of list2) because it is found simultaneously for both of them. Moving the head pointer ahead by a difference of them. The next one is for searching.

Space Complexity: O(1)

Reason: No extra space is used.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDifference(self, headA: ListNode, headB: ListNode)-> int:
        len1, len2 = 0, 0
        tempA, tempB = headA, headB
        while tempA:
            len1 += 1
            tempA = tempA.next
        while tempB:
            len2 += 1
            tempB = tempB.next
        return len1 - len2
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        diff = self.getDifference(headA,headB)
        if diff<0:
            while diff != 0:
                headB = headB.next
                diff += 1
        else:
            while diff != 0:
                headA = headA.next
                diff -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
                