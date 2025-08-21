'''

'''


# Brute force

# So.ution 1

'''

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []

        temp = head
        while temp:
          nums.append(temp.val)
          temp = temp.next
        
        l,r = 0, len(nums)-1
        while l<=r:
          if nums[l] != nums[r]:
            return  False
          l += 1
          r -= 1
        return True
        



# Solution 2
'''
Time Complexity: O(2 * N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and compare with the linked list. Both traversals take O(2*N) ~ O(N) time.

Space Complexity: O(N) We use a stack to store the values of the linked list, and in the worst case, the stack will have all N values,  ie. storing the complete linked list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = deque()
        temp = head
        while temp is not None:
            st.append(temp.val)
            temp = temp.next
            
        temp = head
        while temp is not None:
            if temp.val != st.pop():
                return False
            temp = temp.next
        return True



# Optimised approach

'''
O(n) time and O(1) space
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow = head, head
        # find middle (slow is our middle pointer)
        while fast and fast.next:
          fast = fast.next.next
          slow = slow.next
        
        # reverse second half
        prev = None
        while slow:
          tmp = slow.next
          slow.next = prev
          prev = slow
          slow = tmp
        
        # check if its a palindrome 
        left = head
        right = prev
        while right:
          if left.val != right.val:
            return False
          left = left.next
          right = right.next
        
        return True
        
