class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        newnode = node(x)
        if(self.front == None and self.rear == None):
            self.front = self.rear = newnode
            return
        self.rear.next = newnode
        self.rear = newnode
    
    def dequeue(self):
        if(self.front == None):
            return
        elif(self.front == self.rear):
            self.front = self.rear = None
        else:
            self.front = self.front.next
    
    def IsEmpty(self):
        return self.front == None and self.rear == None
    
    def printqueue(self):
        temp = self.front
        while(temp != None):
            print(temp.data, end = ' ')
            temp = temp.next
        print()



q = queue()
q.enqueue(8)    # 8
q.enqueue(9)    # 8 9 
q.enqueue(4)    # 8 9 4
q.enqueue(3)    # 8 9 4 3 
q.printqueue() # 8 9 4 3
q.dequeue()     # dequeue 8
q.printqueue() # 9 4 3
