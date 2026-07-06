"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapNodes = {None:None}
        if not head:
            return None
        curr = head
        while curr:
            mapNodes[curr]= Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            newN = mapNodes[curr]
            newN.next = mapNodes[curr.next]
            newN.random = mapNodes[curr.random]
            curr = curr.next

        return mapNodes[head]