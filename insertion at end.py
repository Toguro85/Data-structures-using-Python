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
    def insertion_end(self,data):
        new_node=node(data)
        current=self.head

        
        if self.head==None:
            self.head=new_node
        else:
            while (current.get_next()!=None):
                current=current.get_next()
            current.next=new_node
            
    def traverse(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.get_next()
               
        
            #print(current.data)


            

llist=linked_list()
llist.head=node(12)
n2=node(23)
n3=node(2234)
n4=node(36)
llist.head.next=n2
n2.next=n3
n3.next=n4
llist.insertion_end(123)
llist.traverse()
