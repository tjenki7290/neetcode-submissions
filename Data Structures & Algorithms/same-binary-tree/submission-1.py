# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #three base cases 
        if not p and not q: #if they're both None
            return True
        if not p or not q or p.val != q.val: #if one tree's root is None return False or if the values of both roots aren't equal
            return False

        #if it passes all three base cases then make a recusive call of isSameTree to loop through both trees left and right nodes
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

