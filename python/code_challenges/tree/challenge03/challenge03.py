# Write here the code challenge solution


# create node class
'''
this class has three attributes: value, left, right
'''
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# create function that takes an Array and stores To BST
def sortedArrayToBST(num):
        if not num:
            return None
        num.sort()
        mid = len(num) // 2
        print(num[mid])
        root = TreeNode(num[mid])
        root.left = sortedArrayToBST(num[:mid])
        root.right = sortedArrayToBST(num[mid+1:])
        return root

# create breadth first search function
def Breadth(root):    
        x=root
        l=[x]
        final_res=[]
        while l:
            pop_node=l.pop(0)
            final_res.append(pop_node.val)
            if pop_node.left is not None :
                l.append(pop_node.left)
            if pop_node.right is not None:
                l.append(pop_node.right)
        return final_res

 

# Running the code
if __name__ == "__main__":

    tree = TreeNode()
    num=[0,-3,-10,5,9]

    tree.root = sortedArrayToBST(num)
    print(tree.root.val)

    print(Breadth(tree.root))
