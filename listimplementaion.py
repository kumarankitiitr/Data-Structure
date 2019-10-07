class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, node_data):
        newnode = node(node_data)
        if(self.head != None):
            newnode.next = self.head
        self.head = newnode

def printLinkedList(head):
    temp = head
    while(temp != None):
        print(temp.data,end = " ")
        temp = temp.next
    print()

def delete(head, position):
    temp1 = head
    if(position == 1):
        head = temp1.next
    for i in range(position-2):
        temp1 = temp1.next
    temp2 = temp1.next
    temp1.next = temp2.next




l1 = LinkedList()
l1.insert(5) # 5
l1.insert(7) # 7 5
l1.insert(6) # 6 7 5
printLinkedList(l1.head)
delete(l1.head, 2) # 7
printLinkedList(l1.head)
