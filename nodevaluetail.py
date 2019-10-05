def getNode(head, positionFromTail):
    temp = head
    n = 0
    while(head != None):
        if(n > positionFromTail):
            temp = temp.next
        n = n+1
        head = head.next
    return temp.data
