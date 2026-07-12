# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            temp = []
            for node in q:
                temp.append(node.val)
            ans.append(temp)
            r = []
            for node in q:
                if node.left:
                    r.append(node.left)
                if node.right:
                    r.append(node.right)
            q = r

        return ans