# Write your test here


from LinkedList import LinkedList, Node
from challenge01 import *








def test1():
    linkedlist=LinkedList()
    node1=Node(4)
    node2=Node(5)
    node3=Node(1)
    node4=Node(9)

    linkedlist.append(node1)
    linkedlist.append(node2)
    linkedlist.append(node3)
    linkedlist.append(node4)
    delete_node(node2)
    expected = [4,1,9]
    assert linkedlist.printAll() == expected