# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def height(self, root) -> int: # indicates return will be an integer
    # Check for a value in root node
    if root is None:
      # if root node is empty return 0
      return 0
    else:
      # if root node is not empty, find max height on either left or right side of tree and add one
      # return the value
      return 1 + max(self.height(root.left), self.height(root.right))    
    
    
  def isBalanced(self, root: TreeNode) -> bool: # indicates return will be a boolean
    # check for a value in root node
    if root == None:
      # empty root node == balanced => return true
      return True
    # if it's not empty, find the height of the left and right sides then compare them to find if they're balanced and return the boolean
    else: return abs(self.height(root.left) - self.height(root.right)) <= 1 and (self.isBalanced(root.left) and self.isBalanced(root.right))
        
        
    
        
    
        
       
        