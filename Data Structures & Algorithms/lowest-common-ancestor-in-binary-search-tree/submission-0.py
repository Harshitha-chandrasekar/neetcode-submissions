# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None:
            return None

        if p.val == root.val or q.val == root.val:
            return root

        x = self.lowestCommonAncestor(root.left,p,q)
        y = self.lowestCommonAncestor(root.right,p,q)

        if x and y:
            return root

        return x if x else y

        