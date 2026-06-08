# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        point1=l1
        point2= l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while point1 or point2 or carry:
            v1 = point1.val if point1 else 0
            v2 = point2.val if point2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if point1:
                point1 = point1.next
            if point2:
                point2 = point2.next

        return dummy.next
            


    
        