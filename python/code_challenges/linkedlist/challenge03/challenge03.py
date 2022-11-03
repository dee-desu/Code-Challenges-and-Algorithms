# Write here the code challenge solution

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def append(self, value):
        New_Node = Node(value)
        New_Node.next = self.head
        self.head = New_Node
 
    def printAll(self):
        lis=[]
        temp = self.head
        while temp != None:
            lis.append(temp.value)
            temp = temp.next
        return lis

    def deleteNthNode(self, head, n):
        thunder = head
        bolt = head
    
        for i in range(n):
            if thunder.next is None:
                if i==(n-1):
                    self.head = self.head.next
                return self
            thunder = thunder.next  
        while thunder.next:
            thunder = thunder.next
            bolt = bolt.next
    
        bolt.next = bolt.next.next
        return head
        
        
    

 
if __name__ == '__main__':
    l = LinkedList()
    l.append(5)
    l.append(4)
    l.append(3)
    l.append(2)
    l.append(1)
    print('***** Linked List Before deletion *****')
    print(l.printAll()
 )
    l.deleteNthNode(l.head, 1)
 
    print('*********** Linked List after Deletion *****')
    print(l.printAll())



    l = LinkedList()
    l.append(2)
    l.append(1)
    print('***** Linked List Before deletion *****')
    print(l.printAll())
 
    l.deleteNthNode(l.head, 1)
 
    print('*********** Linked List after Deletion *****')
    print(l.printAll())

    l = LinkedList()
    l.append(1)
    print('***** Linked List Before deletion *****')
    print(l.printAll())
 
    l.deleteNthNode(l.head, 1)
 
    print('*********** Linked List after Deletion *****')
    print(l.printAll())
