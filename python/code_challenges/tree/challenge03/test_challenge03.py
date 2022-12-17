# Write your test here

from challenge03 import Breadth,sortedArrayToBST,TreeNode

# test nums=[0,-3,-10,5,9]
def test1():
    nums=[0,-3,-10,5,9]
    assert Breadth(sortedArrayToBST(nums))==[0, -3, 9, -10, 5]

# test nums= [3, 1]
def test2():
    nums= [3, 1]
    assert Breadth(sortedArrayToBST(nums))==[3,1]  