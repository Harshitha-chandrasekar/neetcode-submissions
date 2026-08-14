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
        q = deque()
        q.append([root])
        ans = []
        while q:
            level = q.popleft()
            tempans = []
            nextlev = []
            for node in level:
                if node:
                    tempans.append(node.val)
                    if node.left:
                        nextlev.append(node.left)
                    if node.right:
                        nextlev.append(node.right)
            
            if nextlev:
                q.append(nextlev)
            ans.append(tempans)

        return ans

