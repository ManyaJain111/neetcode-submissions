# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return None
        temp= head
        count=0
        while temp:
            count= count+1
            temp= temp.next
        print(count)
        if n== count:
            return head.next
        if n >count:
            return head
        else:
            skip= count-n
        temp=head
        for i in range(1,skip):
            temp= temp.next
        temp.next=temp.next.next
        return head

            
