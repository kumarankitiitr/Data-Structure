class stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def top(self):
        if(self.items == []):
            return "queue is empty\n"
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    def printstack(self):
        for i in self.items:
            print(i, end = " ")
        print()

s = stack()
s.push(8) # 8
s.push(3) # 8 3
s.push(5) # 8 3 5
s.push(2) # 8 3 5 2
s.printstack()
s.pop()   # 2
s.printstack()
