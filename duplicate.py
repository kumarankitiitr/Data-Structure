def removeDuplicates(head):
    current = head
    if(current == None or current.next == None):
        return head
    else:
        while(current.next != None):
            if(current.data == current.next.data):
                current.next = current.next.next
            else:
                current = current.next
        return head
