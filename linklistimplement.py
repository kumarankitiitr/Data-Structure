class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
    
    def push(self,x):
        newnode = node(x)
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if(self.top == None):
            return
        self.top = self.top.next
    
    def printstack(self):
        temp = self.top
        while(temp != None):
            print(temp.data, end=' ')
            temp = temp.next
        print()

s = stack()
s.push(8) # 8
s.push(3) # 3 8
s.push(5) # 5 3 8
s.push(2) # 2 5 3 8
s.printstack()
s.pop()   # 2
s.printstack()
