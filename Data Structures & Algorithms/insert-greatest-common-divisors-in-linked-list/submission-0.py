# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x
        if not head:
            return None
        curr = head
        nextt = head.next
        while nextt:
            insertval = gcd(curr.val,nextt.val)
            insertNode = ListNode(insertval,nextt)
            curr.next = insertNode
            curr = curr.next.next
            nextt = curr.next

        return head
                    