# Write here the code challenge solution

class Node:
    
    # Function to initialise the node object
    def __init__(self, value):
        self.value = value  
        self.next = None  
    
# Linked List class
class LinkedList:
    
    def __init__(self):
        self.head = None
  
    # Function to insert a new node at the beginning 
    def append(self, new_value): 
        new_node = Node(new_value) 
        new_node.next = self.head 
        self.head = new_node
  
    # Print the linked list
    def printAll(self):
        node = self.head
        l=[]
        while node:
            l.append(node.value)
            node = node.next
        return l
    
    #  Function to get the middle of the linked list
    
    def printMiddle(n):
        if n is None:
            return None
        else:
            middle = n.head
            middle_next = n.head
            while middle_next and middle_next.next is not None:
                middle = middle.next
                middle_next = middle_next.next.next
            return middle


  
# Code execution 
if __name__=='__main__':
    
    # Start with the empty list
    llist = LinkedList()
    
    for i in range(5, 0, -1):
        llist.append(i)

    print(llist.printAll())
    print(llist.printMiddle().value)

    
    llist = LinkedList()
    for i in range(6, 0, -1):
        llist.append(i)

    print(llist.printAll())
    print(llist.printMiddle().value)
    
