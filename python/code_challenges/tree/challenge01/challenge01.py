# Write here the code challenge solution

'''
We want to create a tree depending on the preorder, inorder
'''
# tree node class
class TreeNode():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# pre order function
def pre_order(x,root):
    if root is not None:
        x.append(root.value)
    if root.left is not None:
        pre_order(x,root.left)
    if root.right is not None:
        pre_order(x,root.right)
    return x
# function to build tree
def buildTree( preorder, inorder):

    if inorder:
        INDEX = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[INDEX])
        root.left = buildTree(preorder, inorder[:INDEX])
        root.right = buildTree(preorder, inorder[INDEX+1:])
        return root


#  testing for the above
if __name__ =="__main__":

    tree1 = TreeNode()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    tree1.root = buildTree( preorder, inorder)
    print(pre_order([],tree1.root))

    preorder = [-1]
    inorder = [-1]
    tree1.root = buildTree( preorder, inorder)
    print(pre_order([],tree1.root))
