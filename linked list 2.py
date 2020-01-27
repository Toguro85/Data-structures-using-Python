#insertion
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
    def insertion_beg(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def insertion_after(self,prev_node,data):
        if prev_node==None:
            self.insertion_beg(data)
        else:
            new_node=node(data)
            new_node.next=prev_node.get_next()
            prev_node.next=new_node
    def traverse_ll(self):
        count=0
        current=self.head
        while(current!=None):
          print(current.data)
          count=count+1
          current=current.get_next()
        print("count",count)
            
            
llist=linked_list()
llist.head=node(1)
n2=node(3)
n3=node(5)
llist.head.next=n2
n2.next=n3
llist.insertion_beg(2)
llist.insertion_after(n2,3)
llist.traverse_ll()

        
