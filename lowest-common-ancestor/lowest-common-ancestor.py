# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None: #Base Case
            return None
        
        if root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q) #Check Left Nodes 
        right = self.lowestCommonAncestor(root.right,p,q) #Check Right Nodes
        
        if left!=None and right!=None: #Pass Node to root 
            return root
        if left==None and right==None: #Pass None to root
            return None
        
        return left if left else right