# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        h = newNode
        while list1 and list2:
            if list1.val>=list2.val:
                newNode.next = list2
                newNode = newNode.next
                list2 = list2.next
            else:
                newNode.next = list1
                newNode = newNode.next
                list1 = list1.next

        if list1:
            newNode.next = list1

        if list2:
            newNode.next = list2

        return h.next