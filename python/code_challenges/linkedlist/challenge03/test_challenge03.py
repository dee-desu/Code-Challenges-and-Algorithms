# Write your test here

from challenge03 import LinkedList, Node

def test1():
    l = LinkedList()
    l.append(1)
    l.deleteNthNode(l.head, 1)
    actual = l.printAll()
    expected = []
    assert actual == expected


def test12():
    l = LinkedList()
    l.append(2)
    l.append(1)
    l.deleteNthNode(l.head, 1)
    actual = l.printAll()
    expected = [1]
    assert actual == expected

    # input = [1, 2]


def test13():
    l = LinkedList()
    l.append(5)
    l.append(4)
    l.append(3)
    l.append(2)
    l.append(1)
    l.deleteNthNode(l.head, 1)
    actual = l.printAll()
    expected = [1,2,3,4]
    assert actual == expected
