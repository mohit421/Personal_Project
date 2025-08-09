

class node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None 

class linked_list:
    def __init__(self):
        self.head = node()

    # append in linked list
    def append(self, data):
        new_node = node(data)
        curr = self.head 
        while curr.next != None:
            curr = curr.next 
        curr.next = new_node 
    
    # length of Linked list
    def length(self):
        curr = self.head 
        total = 0
        while curr.next != None:
            total += 1
            curr = curr.next 
        return total 

    # display current content of list
    def display(self):
        elems = []
        curr_node = self.head 
        while curr_node.next != None:
            curr_node=curr_node.next
            elems.append(curr_node.data)
        print(elems)
    
    # this will pull out data at certain index from the linked list ( Extractor)
    def get(self,index):
        if index >= self.length():
            print("Error: 'Get' Index Out Of Range")
            return None 
        curr_idx = 0
        curr_node = self.head 
        while True:
            curr_node = curr_node.next 
            if curr_idx == index:
                return curr_node.data 
            curr_idx += 1

    # Erase function

    def erase(self, index):
        if index >= self.length():
            print("Error: 'Erase' Index out of Range!")
            return 
        curr_idx = 0
        curr_node = self.head 
        while True:
            last_node = curr_node
            curr_node  = curr_node.next
            if curr_idx == index:
                last_node.next = curr_node.next 
                return 
            curr_idx += 1
my_list = linked_list()

my_list.display()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list.erase(1)
my_list.display()
print("Element at 2nd Index: %d", my_list.get(3))


'''
Leetcode problem 
707 Design Linkedlist 
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index<0 or index >= self.size:
            return -1
        curr_node = self.head
        for _ in range(0,index):
            curr_node = curr_node.next
        return curr_node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        curr_node = self.head
        new_node = ListNode(val)
        if index<=0:
            new_node.next = curr_node
            self.head = new_node
        else:
            for _ in range(index-1):
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>= self.size:
            return

        curr_node = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0,index-1):
                curr_node = curr_node.next
            curr_node.next = curr_node.next.next
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


'''
with the help of above code using my ways 
'''

class node:
    def __init__(self, val):
        self.val = val
        self.next = None 
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index>=self.size:
            return -1
        curr_idx = 0
        curr_node = self.head
        while curr_node:
            if curr_idx == index:
                return curr_node.val
            curr_node = curr_node.next
            curr_idx += 1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        curr_node = self.head
        new_node = node(val)
        if index<=0:
            new_node.next = curr_node
            self.head = new_node
        else:
            for _ in range(index-1):
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node
        self.size += 1
    


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index>= self.size:
            return
        curr_node = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                curr_node = curr_node.next
            curr_node.next = curr_node.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# same using while loop

class node:
    def __init__(self, val):
        self.val = val
        self.next = None 
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index>=self.size:
            return -1
        curr_idx = 0
        curr_node = self.head
        while curr_node is not None:
            if curr_idx == index:
                return curr_node.val
            curr_node = curr_node.next
            curr_idx += 1
        return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        # curr_node = self.head
        new_node = node(val)
        if index<=0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node  = self.head
            curr_idx = 0
            while curr_idx < index-1:
                curr_node = curr_node.next
                curr_idx += 1
            new_node.next = curr_node.next
            curr_node.next = new_node
        self.size += 1
    


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index>= self.size:
            return
        curr_node = self.head

        if index == 0:
            self.head = self.head.next
        else:
            curr_node = self.head
            curr_idx = 0
            while curr_idx < index - 1:
                curr_node = curr_node.next
                curr_idx += 1
            curr_node.next = curr_node.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
