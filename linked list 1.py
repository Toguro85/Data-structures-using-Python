class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def get_next(self):
        return self.next
class linked_list:
    def __init__(self):
        self.head=None
    def traverse_ll(self):
        count=0
        current=self.head
        while(current!=None):
            print(current.data)
            count=count+1
            current=current.get_next()
        print("count",count)
llist=linked_list()
llist.head=Node(5)
n2=Node(6)
n3=Node(7)
llist.head.next=n2
n2.next=n3
llist.traverse_ll()



