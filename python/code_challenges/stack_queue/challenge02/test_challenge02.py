# Write your test here

from challenge02 import Valid_Parentheses

def test_1():
    v=Valid_Parentheses()
    
    assert v.isValid('()') == True



def test_2():
    v=Valid_Parentheses()
    
    assert v.isValid('{}') == True

def test_3():
    v=Valid_Parentheses()
    
    assert v.isValid('()[]') == True


def test_4():
    v=Valid_Parentheses()
    
    assert v.isValid('{}()[]') == True