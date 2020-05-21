class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None

def findPath(root,path,k):
    if root is None:
        return False
    path.append(root.key)
    if root.key==k:
        return True
    if ((root.left!=None and findPath(root.left,path,k)) or (root.right!=None and findPath(root.right,path,k))):
        return True
    path.pop()
    return False

def findLCA(root,n1,n2):
    path1=[]
    path2=[]
    if (not findPath(root,path1,n1) or not findPath(root,path2,n2)):
        return -1
    i=0
    while (i<len(path1) and i<len(path2)):
        if path1[i]!=path2[i]:
            break
        i+=1
    return path1[i-1]

root=Node(20)
root.right=Node(22)
root.left=Node(8)
root.left.left=Node(4)
root.left.right=Node(12)
root.left.right.left=Node(10)
root.left.right.right=Node(14)

'''
                      20
                    /    \
                   8      22
                  /  \
                 4    12
                    /    \
                   10     14
'''

print("LCA of 10 and 14 is",findLCA(root,10,14))
print("LCA of 14 and 8 is",findLCA(root,14,8))
print("LCA of 10 and 22 is",findLCA(root,10,22))
