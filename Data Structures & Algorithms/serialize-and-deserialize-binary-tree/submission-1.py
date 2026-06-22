# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Serialize and Deserialize Binary Tree
# Implement an algorithm to serialize and deserialize a binary tree.
# Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

# ************ Using array ran into time limit exceeded ************

class Codec:
    delimiter = ","
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        # preorder
        def dfs(node):
            if not node:
                res.append("n")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return self.delimiter.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: 
            return None
            
        vals = data.split(self.delimiter)
        # Use an iterator to cleanly consume values one by one
        vals_iter = iter(vals)
        print(data)
        
        def construct() -> Optional[TreeNode]:
            val = next(vals_iter)
            if val == "n":
                return None
                
            node = TreeNode(int(val))
            node.left = construct()
            node.right = construct()
            return node
        
        return construct()
