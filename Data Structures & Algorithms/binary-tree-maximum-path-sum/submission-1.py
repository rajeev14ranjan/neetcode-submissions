# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Binary Tree Maximum Path Sum
# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.
# The path sum of a path is the sum of the node's values in the path.
# ***** similar to diameter of tree problem ******

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = -math.inf

        def pathsum(node: Options[TreeNode]) -> int:
            nonlocal maxsum
            if node is None: return 0

            # max pathsum of left and right subtree 
            # handle negative values
            leftsum = max(0 , pathsum(node.left))
            rightsum = max(0, pathsum(node.right))

            # max path sum if path is split at currenet node, i.e left -- node -- right side as path
            maxsum = max(maxsum, leftsum + node.val + rightsum)

            # while returning, we need to return the pathsum without spliting. node --left or node --right
            return node.val + max(leftsum, rightsum)
        
        pathsum(root)
        return maxsum