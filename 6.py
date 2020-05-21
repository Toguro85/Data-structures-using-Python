'''
The given binary tree is not a Binary Search Tree (BST) then print the location of 1 st violation.
'''
class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None

def isBSTUtil(node,min1,max1):
    if node is None:
        return True
    
    if node.key<min1 or node.key>max1:
        print("Location of 1st Violation: Level",getLevel(root,node.key))
        return False
    
    return (isBSTUtil(node.left,min1,node.key-1)and isBSTUtil(node.right,node.key+1,max1))

int_min=-4294967296
int_max=4294967296

def isBST(node):
    return (isBSTUtil(node,int_min,int_max))

def getLevelUtil(node,key,level):
    if node is None:
        return 0
    if node.key==key:
        return level
    downlevel=getLevelUtil(node.left,key,level+1)
    if (downlevel!=0):
        return downlevel
    downlevel=getLevelUtil(node.right,key,level+1)
    return downlevel

def getLevel(root,key):
    return getLevelUtil(root,key,1)#level start from 1

root=Node(12)
root.right=Node(15)
root.left=Node(8)
root.left.right=Node(6)
root.left.left=Node(10)
root.right.left=Node(14)
root.right.right=Node(16)

'''
                 12 ------------- Level 1
              /      \
            8          15 ------- Level 2
           /  \        /   \
        10     6     14     16 -- Level 3
'''

if (isBST(root)):
    print("is BST")
else:
    print("Not a BST")
    
