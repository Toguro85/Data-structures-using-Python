class stack:
    def __init__(self,limit=10):
        self.stk=[]
        self.limit=limit

    def isfull(self):
        if len(self.stk)==self.limit:
            return True
    def push(self,data):
        if (self.isfull()):
            print("stack is full")
        else:
            self.stk.append(data)
            print("stack after insert is:",self.stk)

    def isempty(self):
        if len(self.stk)==0:
            return True

    def pop(self):
        if (self.isempty()):
            print("stack is empty")
        else:
            self.stk.pop()
            print("stac is:",self.stk)

    def top(self):
        if (self.isempty()):
            print("stack is empty")
        else:
            print("top item is :",self.stk[-1])


stack1=stack(2)
#stack1.push(28)
#stack1.push(2)
#stack1.push(82)
stack1.pop()
