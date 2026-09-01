# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True #both roots = None 
        if not p or not q or p.val != q.val: #checking to see if one root is None and the other isn't, also checking to see if the values are the same
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)