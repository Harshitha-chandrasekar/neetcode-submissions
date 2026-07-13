# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def check(node,maximum):
            if not node:
                return 0
            if node.val>=maximum:
                return 1 + check(node.left,node.val) + check(node.right,node.val)

            return check(node.left,maximum) + check(node.right,maximum)

        if not root:
            return count
        
        return check(root,root.val)
