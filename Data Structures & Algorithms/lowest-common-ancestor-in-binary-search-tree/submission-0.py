# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # search subtree based on the value of p and q 
        # for example if p and q are greater than the root then we can just start our search on the right side, vice versa if the two values are less than the root, do this recrusivly until we run into a split...
        # if the values are split then we will return that ancestor, beacaude wherever there is a split that is where the LCA lives
        # the last edge case: if one of the nodes is equal to the root node then we need to return that node as the LCA
        node = root 
        while node: #node is never going to reach None beacuase there is always a guaranteed LCA 
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left  
            else:
                return node

        

