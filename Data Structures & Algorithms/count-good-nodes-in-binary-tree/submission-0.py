# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(root,val):
            if root is None:
                return 0
            good = 1 if root.val >= val else 0

            val = max(val, root.val)

            return good + count(root.left, val) + count(root.right, val)

        return count(root, root.val)