# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def getLastNode(h):
            while h.next.next:
                h = h.next
            lastN = h.next
            h.next = None
            return lastN

        temp = head
        while temp.next and temp.next.next:
            insert = getLastNode(temp)
            insert.next = temp.next
            temp.next = insert
            temp = temp.next.next
