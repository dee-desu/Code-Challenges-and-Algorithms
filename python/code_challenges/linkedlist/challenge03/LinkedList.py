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
  
  
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next