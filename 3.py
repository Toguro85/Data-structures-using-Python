'''
Find the minimum value in a Binary Search Tree (BST) and print its location.
'''

class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None

def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.key:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root

def minValue(root):
    current=root
    while (current.left is not None):
        current=current.left
    return current.key

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

root=Node(3)
insert(root,2) 
insert(root,5) 
insert(root,1) 
insert(root,4)

'''
         3 ----------- Level 1
       /    \
       2     5 ------- Level 2
       /    /
       1    4  ------- Level 3
'''

node=minValue(root)
print("Minimum value in the BST :",node)
level=getLevel(root,node)
print("Loaction of node is : Level",level)
