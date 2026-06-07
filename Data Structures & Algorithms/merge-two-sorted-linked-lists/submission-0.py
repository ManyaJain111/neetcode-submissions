# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        point1= list1
        point2= list2
        list3= ListNode(0)
        point3= list3
        while point1 and point2:
            if point1.val>point2.val:
                point3.next=point2
                point2= point2.next
            else:
                point3.next= point1
                point1= point1.next
            point3= point3.next
        while point1:
            point3.next= point1
            point1= point1.next
            point3=point3.next
        while point2:
            point3.next= point2
            point2= point2.next
            point3=point3.next
        return list3.next


