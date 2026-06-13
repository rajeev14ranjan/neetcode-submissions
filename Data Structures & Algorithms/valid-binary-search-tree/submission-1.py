# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], minval, maxval) -> bool:
            if node is None:
                return True

            if not (minval < node.val < maxval):
                return False

            return dfs(node.left, minval, min(maxval, node.val)) and dfs(
                node.right, max(minval, node.val), maxval
            )

        return dfs(root, -math.inf, math.inf)
