# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Binary Tree Right Side View
# You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.
# *************** Good Improv ***************


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque()
        q.append(root)
        view = []

        while q:
            lvl_count = len(q)
            for i in range(lvl_count):
                node = q.popleft()
                if i == 0:  # first elt in this level from right
                    view.append(node.val)

                # append right first
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return view
