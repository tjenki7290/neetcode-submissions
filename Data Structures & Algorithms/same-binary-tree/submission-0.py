# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #if both roots are None then they are the same so return True
            return True
        if not p or not q or p.val != q.val: #so if one root is None and the other is not return False
            return False #the last base case, both are not None so you have to check if their values are the same

    #if all these tests pass then you need to use recursion for the left and right sides of both trees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

