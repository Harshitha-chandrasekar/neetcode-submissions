# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag = True
        def check(p,q):
            if not p and not q:
                return
            if not p or not q:
                self.flag = False
                return

            if p.val != q.val:
                self.flag = False
                return

            check(p.left,q.left)
            check(p.right,q.right)

        check(p,q)
        return self.flag