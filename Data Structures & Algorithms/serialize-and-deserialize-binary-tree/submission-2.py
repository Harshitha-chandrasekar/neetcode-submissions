# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        s = []
        def ser(root):
            if not root:
                s.append('N')
                return 
            s.append(str(root.val))
            ser(root.left)
            ser(root.right)
        ser(root)
        news = ",".join(s)
        return news
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        vals = iter(data.split(","))

        def deser():
            val = next(vals)

            if val == 'N':
                return None

            node = TreeNode(int(val))

            node.left = deser()
            node.right = deser()
            
            return node

        return deser()