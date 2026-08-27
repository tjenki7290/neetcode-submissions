# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #you cant start the comparison until the root of subRoot equals the current node of root
        def sameTree(p,q):
            if not p and not q: 
                return True
            if not p or not q or p.val != q.val:
                return False 

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def has_subtree(root):
            if not root: #if we search all the way through to None then we return False
                return False
            
            if sameTree(root, subRoot):
                return True

            return has_subtree(root.left) or has_subtree(root.right)


        return has_subtree(root)

            
