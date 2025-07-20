from LinkedLists.Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    """
        Print all the elements of the linkelist
    """
    def printLinkedList(self):
        if self.head is None:
            return
        curr = self.head
        elements = []
        while curr:
            elements.append(curr.value)
            curr = curr.next
        print(elements) 
    
    """
        Search for an given element in the linked list
    """
    def searchElement(self, element):
        if self.head is None:
            return False
        curr = self.head
        while curr:
            if curr.value == element:
                return True
        return False
    
    """
        Add a node at starting of the linked list
    """
    def addNodeStarting(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    
    """
        Add a node at the end of the linked list
    """
    def addAtEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        self.head = curr

    """
        Returns the length and last node of the linked list
    """
    def findLength(self):
        if self.head is None:
            return -1, None
        len = 1
        curr = self.head
        while curr.next:
            curr = curr.next
            len += 1
        return len, curr
    
    """
        Finds the middle element of the linked list
        using fast and slow pointer approach 
    """
    def findMiddleElement(self):
        if self.head is None:
            return 
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print(slow.value)
        
    """
        Reverse the current linked list
    """
    def reverseLinkedList(self):
        if self.head is None:
            return 
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        
    """
        Rotate the linked list from right based on the
        Nth element/node
    """
    def rotateLinkedList(self, n):
        if self.head is None:
            return 
        curr = self.head 
        listLen, tail = self.findLength()
        n = n%listLen
        if listLen == 1 or n == 0 or n == listLen:
            return
        for i in range(listLen - n - 1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        tail.next = self.head
        self.head = newHead