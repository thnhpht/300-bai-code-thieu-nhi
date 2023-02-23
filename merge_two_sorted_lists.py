from tkinter.tix import ListNoteBook


def mergeTwoLists(list1, list2):
    while list1 and list2:
            if list1.val<=list2.val:
                curr.next=ListNode(list1.val)
                list1=list1.next
            else:
                curr.next=ListNode(list2.val)
                list2=list2.next
            curr=curr.next
        
    while list1:
        curr.next=ListNode(list1.val)
        list1=list1.next
        curr=curr.next
    
    while list2:
        curr.next=ListNoteBook(list2.val)
        list2=list2.next
        curr=curr.next
                
    return ans.next

list1 = []
list2 = [0]

result = mergeTwoLists(list1, list2)
print(result)
    