# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def h(root):
            if not root:
                return 0
            hl = h(root.left)
            hr = h(root.right)
            return max(hl,hr) + 1        
        
        if not root:
            return True

        hleft = h(root.left)
        hright = h(root.right)

        if abs(hleft - hright) <= 1:
            flag = True
        else:
            flag = False

        return flag and self.isBalanced(root.left) and self.isBalanced(root.right)