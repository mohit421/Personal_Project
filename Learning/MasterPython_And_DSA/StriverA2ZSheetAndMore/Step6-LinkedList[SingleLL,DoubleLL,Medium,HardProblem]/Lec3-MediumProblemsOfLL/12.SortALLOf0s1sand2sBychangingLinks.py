'''

'''

# Brute force
'''

'''

'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    def segregate(self, head):
        #code here
        cnt0, cnt1, cnt2 = 0,0,0
        
        temp = head
        while temp:
            if temp.data == 0:
                cnt0 += 1
            elif temp.data == 1:
                cnt1 += 1
            else:
                cnt2 += 1
            temp  = temp.next
        curr = head
        
        while cnt0:
            curr.data = 0
            curr = curr.next
            cnt0 -= 1
        while cnt1:
            curr.data = 1
            curr = curr.next
            cnt1 -= 1
        while cnt2:
            curr.data = 2
            curr = curr.next
            cnt2 -= 1
        
        return head
    

# Optimised sol

'''
TC:- O(N)
SC:- O(1)
'''


'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    def segregate(self, head):
        #code here
        if head is None or head.next is None:
            return head
            
        # Dummy heads
        zeroHead, oneHead, twoHead = Node(-1), Node(-1), Node(-1)
        zero, one, two = zeroHead, oneHead, twoHead
        
        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next
        
        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None
        return zeroHead.next