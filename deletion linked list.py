class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def get_next(self):
        return self.next
    def get_data(self):
        return self.data
class linked_list:
    def __init__(self):
        self.head=None
    def deletion_beg(self):
        if self.head==None:
            print("deletion is not possible")
        else:
            current=self.head
            self.head=current.get_next()

    def deletion_end(self):
        if self.head==None:
            return ("deletion not possible")
        else:
            prev=self.head
            current=self.head
            while current.next!=None:
                prev=current
                current=current.get_next()
            prev.next=None

    
    def traverse(self):
        current=self.head
        while (current!=None):
            print(current.data)
            current=current.get_next()


            
llist=linked_list()
llist.head=node(23)
n2=node(546)
n3=node(758)
n4=node(30)
llist.head.next=n2
n2.next=n3
n3.next=n4
llist.deletion_beg()
llist.deletion_end()
llist.traverse()






