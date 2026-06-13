# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Diameter of Binary Tree
# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
# The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.

# dia counts no of edges and not nodes. height count no of nodes down on that side.
# ******************* not easy - couple of gotchas
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxheightdia(node):
            if not node:
                return 0, 0

            leftheight, leftdia = maxheightdia(node.left)
            rightheight, rightdia = maxheightdia(node.right)
            current_height = 1 + max(leftheight, rightheight)

            # The diameter is the longest path between any two nodes, measured in edges
            # leftheight counts the nodes below on left side -> or no of edges on left side.
            # same for rightSide -> Hence we don't need "leftheight + rightheight + 1"
            current_max_dia = max(leftheight + rightheight, leftdia, rightdia)

            return current_height, current_max_dia

        height, max_dia = maxheightdia(root)
        return max_dia
