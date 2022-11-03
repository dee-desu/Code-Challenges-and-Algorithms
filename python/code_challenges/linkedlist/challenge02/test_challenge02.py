# Write your test here
from challenge02 import LinkedList

def test1():
    llist = LinkedList()

    for i in range(5, 0, -1):
        llist.append(i)

    print(llist.printAll())
    
    actual = llist.printMiddle().value
    expected = 3
    assert actual == expected


def test2():
    llist = LinkedList()

    for i in range(6, 0, -1):
        llist.append(i)

    print(llist.printAll())
    
    actual = llist.printMiddle().value
    expected = 4
    assert actual == expected
