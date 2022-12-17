# Write your test here

from challenge01 import buildTree,pre_order,TreeNode

# test 1
'''
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
'''
def test1():
    tree=TreeNode()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    tree.root = buildTree( preorder, inorder)
    assert pre_order([],tree.root)==[3,9,20,15,7]


# test 2
'''
preorder = [-1]
inorder = [-1]
'''
def test2():
    tree=TreeNode()
    preorder = [-1]
    inorder = [-1]
    tree.root = buildTree( preorder, inorder)
    assert pre_order([],tree.root)== [-1]
