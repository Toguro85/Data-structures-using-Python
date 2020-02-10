class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class stack_ll:
    def __init__(self):
        self.head=None
        
    def isempty(self):
        
        if self.head==None:
            return True
        else:
            return False
    
    def push(self,data):
        
        if self.isempty():
            self.head=node(data)
           
        else:
            newnode=node(data)
            newnode.next=self.head
            self.head=newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            currentnode=self.head
            self.head=self.head.next
            currentnode.next=None
        return currentnode.next

    def top(self):
        if self.isempty():
            print("stack is empty")
        else:
            print( self.head.data)
           

    def display(self):
        current=self.head
        if self.isempty():
            print("stack underflow")
        else:
            while (current!=None):
                print(current.data,"->",end=" ")
                current=current.next


stack1=stack_ll()
stack1.push(3)
stack1.push(37)
stack1.push(2)
stack1.push(48)
stack1.display()
print("\n")
stack1.pop()
stack1.display()
print("\n")
stack1.top()

