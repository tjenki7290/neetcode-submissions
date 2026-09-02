# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #traverse in order beacause the tree is already sorted BST and we count down k for each node, when k hits 0 that's our answer
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val
            node = node.right

            

