'''
WAP to delete a specific node from the BST and print the post-order traversal for the
same.
'''



class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.key=key
      
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
    return current

def deleteNode(root,key):
    if root is None:
        return root
    if (key<root.key):
        root.left=deleteNode(root.left,key)
    elif (key>root.key):
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValue(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root
        

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key,end=" ")

root=Node(50)
insert(root,30) 
insert(root,20) 
insert(root,40) 
insert(root,70)
insert(root,60)
insert(root,80)

print("Postorder traversal of a given tree")
postorder(root)

print("\n")
print("Enter the node you want to delete")
node=int(input())

deleteNode(root,node)
print("Postorder traversal of modified tree")
postorder(root)



      
