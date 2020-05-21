class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key

def insert(root,node):
    if root is None:
        root=node
    else:
        if root.val<node.val:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)

def search(root,key):
    while root!=None:
        if ascii(key)>ascii(root.val):
            root=root.right
        elif ascii(key)<ascii(root.val):
            root=root.left
        else:
            return True
    return False

root=Node("A")
insert(root,Node("P"))
insert(root,Node("V"))
insert(root,Node("D"))
insert(root,Node("E"))
insert(root,Node("F"))
insert(root,Node("G"))
insert(root,Node("H"))

print("Enter alphabet to be searched")
al=input()

if search(root,al) == True :
    print("Yes")
else:
    print("No")


