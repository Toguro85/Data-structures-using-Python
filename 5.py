class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None

def isBSTUtil(node,min1,max1):
    if node is None:
        return True
    
    if node.key<min1 or node.key>max1:
        return False
    
    return (isBSTUtil(node.left,min1,node.key-1)and isBSTUtil(node.right,node.key+1,max1))

int_min=-4294967296
int_max=4294967296

def isBST(node):
    return (isBSTUtil(node,int_min,int_max))


root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(1)
root.left.right=Node(3)

'''
                 4
              /    \
              2     5
              /\
            1    3
'''

if (isBST(root)):
    print("is BST")
else:
    print("Not a BST")
    
            
