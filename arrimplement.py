class queue:
    def __init__(self):
        self.items = []
    def IsEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def front(self):
        if(self.items == []):
            return "queue is empty\n"
        return self.items[0]
    def rear(self):
        if(self.items == []):
            return "queue is empty\n"
        return self.items[len(self.items)-1]
    def printqueue(self):
        for i in self.items:
            print(i, end = ' ')
        print()

q = queue()
print(q.size()) # 0
q.enqueue(8)    # 8
q.enqueue(9)    # 9 8
q.enqueue(4)    # 4 9 8
q.enqueue(3)    # 3 4 9 8 
q.printqueue() # 3 4 9 8
q.dequeue()     # dequeue 8
q.printqueue() # 3 4 9
print(q.front())
print(q.rear())
