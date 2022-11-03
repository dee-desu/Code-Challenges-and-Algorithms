# Write here the code challenge solution


from LinkedList import LinkedList, Node  


def delete_node(node):
    if node.next is not None:
        node.value  = node.next.value
        node.next = node.next.next



if __name__=="__main__":
    linkedlist=LinkedList()
    node1=Node(4)
    node2=Node(5)
    node3=Node(1)
    node4=Node(9)

    linkedlist.append(node1)
    linkedlist.append(node2)
    linkedlist.append(node3)
    linkedlist.append(node4)
    print(linkedlist.printAll())
    delete_node(node3)
    print(linkedlist.printAll())