# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = newNode = ListNode()
        h1 = list1
        h2 = list2

        while h1 and h2:
            if h1.val < h2.val:
                newNode.next = h1
                h1 = h1.next
            else:
                newNode.next = h2
                h2 = h2.next
            newNode = newNode.next
            
        newNode.next = h1 or h2    
        return head.next

