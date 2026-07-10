# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        def dia(root):
            if root:
                lefth = dia(root.left)
                righth = dia(root.right)
                self.diam =  max(self.diam,lefth+righth)
                return 1+max(lefth,righth)
            else:
                return 0

        dia(root)
        return self.diam