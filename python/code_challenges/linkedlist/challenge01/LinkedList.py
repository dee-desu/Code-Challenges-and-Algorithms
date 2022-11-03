class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) :
        self.head= None
    
    def append(self, node):
        if self.head is None:
            self.head=node
        else:
            current = self.head
            while current.next is not None :
                current = current.next
            current.next = node

    def printAll(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            l=[]
            while current is not None :
                l.append(current.value)
                current = current.next
            return l