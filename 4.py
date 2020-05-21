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

def PreSuc(root,pre,suc,key):
    if root==None:
        return
    while root!=None:
        if root.key==key:
            if root.right:
                suc[0]=root.right
                while suc[0].left:
                    suc[0]=suc[0].left
            if root.left:
                pre[0]=root.left
                while pre[0].right:
                    pre[0]=pre[0].right
            return
        elif root.key<key:
            pre[0]=root
            root=root.right
        else:
            suc[0]=root
            root=root.left

root=Node(50)
insert(root,30)  
insert(root,20)  
insert(root,40)  
insert(root,70)  
insert(root,60)  
insert(root,80)

print("Enter key")
key=int(input())

pre,suc=[None],[None]
PreSuc(root,pre,suc,key)

if pre[0]!=None:
    print("Predecessor is:",pre[0].key)
else:
    print("No Predecessor! No node in the BST has the value less than",key)

if suc[0]!=None:
    print("Successor is:",suc[0].key)
else:
    print("No Successor! No node in the BST has the value greater than",key)
