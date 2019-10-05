# two heads of each list llist1, llist2

def compare_lists(llist1, llist2):
    n =0
    m= 0
    temp1 = llist1
    temp2 = llist2
    while(temp1 != None):
        temp1 = temp1.next
        n += 1
    while(temp2 != None):
        temp2 = temp2.next
        m += 1
    if(n != m):
        return 0
    else:
        temp3 = llist1
        temp4 = llist2
        for i in range(n):
            if(temp3.data == temp4.data):
                temp3 = temp3.next
                temp4 = temp4.next
                continue
            else:
                return 0
        return 1
