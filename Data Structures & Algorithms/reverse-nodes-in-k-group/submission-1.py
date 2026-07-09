# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        master_dummy = ListNode(-1, head)
        group_prev = master_dummy
    
        while True:
            kth = group_prev
            c = 0
            while c < k and kth:
                kth = kth.next
                c += 1
            if not kth:
                break
                
            group_next = kth.next         

            prev, curr = kth.next, group_prev.next
            
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            old_start = group_prev.next             
            group_prev.next = kth 
            group_prev = old_start       

        return master_dummy.next