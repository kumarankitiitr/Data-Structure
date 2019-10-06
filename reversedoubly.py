def reverse(head):
    while head != None:
        nxt = head.next
        curr = head
        head.next = head.prev
        head.prev = nxt
        head = nxt
    
    return curr
