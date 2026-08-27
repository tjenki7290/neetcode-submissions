# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #going to need to make two helpers one is going to check to see if they're the same tree 
        #the other is going to see if a the root contains the subtree and will call the previously made helper
        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val !=  q.val:
                return False
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def has_subtree(root):
            if not root:
                return False

            if sameTree(root, subRoot):
                return True

            return has_subtree(root.left) or has_subtree(root.right)

        return has_subtree(root)

            
