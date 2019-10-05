# first define the node class
class node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
# Class for Linked List and for its methods    
class LinkedList:
    def __init__(self):
        self.head = None
    def insertLast(self, value):
        newNode = node(value)
        if(self.head == None):
            self.head = newNode
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode

#function for print the elements of a linked list
def printlist(head):
    temp = head
    if(temp == None):
        return
    else:
        while(temp != None):
            print(temp.data, end = ' ')
            temp = temp.next

#function for reverse the elemnets of LinkedList using recurrsion
def reverse(head):
    if(head == None or head.next == None):
        return head
    else:
        q = reverse(head.next)  # at end head points to the second last node of list
        head.next.next = head   # make the node points to previous node
        head.next = None        # make previous node to null
        return q                # return the address of new hade

l = LinkedList()
l.insertLast(4)
l.insertLast(8)
l.insertLast(7)
l.insertLast(5)
printlist(l.head)
print()
l1 = reverse(l.head)
printlist(l1)
print()
