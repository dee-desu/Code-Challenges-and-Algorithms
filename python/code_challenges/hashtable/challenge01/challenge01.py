# Write here the code challenge solution

# create node class
class Node():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    # create function that sorted Array To BST
    def sortToBst(self,num):
        num.sort()
        def biTree(nums):
            if not nums:
                return None                                          
            m = len(nums)//2
            return (Node(nums[m],biTree(nums[:m]),biTree(nums[m+1:])) )
        root=biTree(num)
        return root


# pre order function
def ordered(root , x):
    if root is not None:
        x.append(root.value)
    if root.left is not None:
        ordered(root.left , x)
    if root.right is not None:
        ordered(root.right , x)
    return x





# function that takes a Binary Search tree and an integer as a parameter. Return True if Binary search tree has two elements that their summation is the given integer
def summation(root,k):
    x = ordered(root,[])
    for i in range(len(x)):
        if (x[i] - k ) not in x:
            continue
        else:
            return True
    else:
        return False

# to try the function it work 

if __name__ == "__main__":

    tree = Node()
    T=tree.sortToBst([7,2,9,1,5,14])
    print(summation(T,4))
    