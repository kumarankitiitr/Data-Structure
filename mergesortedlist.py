def mergeLists(head1, head2):
    p = head1
    q = head2
    if p== None:
        return q
    if q== None:
        return p
    if(p.data <= q.data):
        s = p
        p = s.next
    else:
        s = q
        q = s.next
    new_head = s

    while(p != None and q != None):
        if(p.data <= q.data):
            s.next = p
            s = p
            p = s.next
        else:
            s.next = q
            s = q
            q = s.next
    if p== None:
        s.next = q
    if q== None:
        s.next = p
    
    return new_head
 
