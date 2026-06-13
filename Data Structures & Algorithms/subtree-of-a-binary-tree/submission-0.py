# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node.val == subRoot.val and self.sametree(node, subRoot): 
                return True
            
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        return False
      

    def sametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif not p or not q: return False
        elif p.val != q.val: return False

        return self.sametree(p.left, q.left) and self.sametree(p.right, q.right)
        