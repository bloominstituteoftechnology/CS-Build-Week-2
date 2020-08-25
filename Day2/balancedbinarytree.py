from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(n: TreeNode) -> int:
            cache = {}
            if n == None:
                return 0
            if n not in cache:
                cache[n] = 1 + max(get_height(n.left), get_height(n.right))
            return cache[n]
        
        if root is None:
            return True
        l_height = get_height(root.left)
        r_height = get_height(root.right)
            
        
        return abs(l_height - r_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
def make_tree(nums: list) -> TreeNode:
    root = TreeNode(nums[0])
    nums = nums[1:]
    i = 0
    q = Queue()
    q.put(root)
    while i < len(nums) - 1:
        cur = q.get()
        l = TreeNode(nums[i:])
        r = TreeNode(nums[i + 1:])
        cur.left = l
        cur.right = r
        i += 2
        q.put(l)
        q.put(r)
    return root

test = Solution()

ex1 = [3,9,20,None,None,15,7]
ex2 = [1,2,2,3,None,None,3,4,None,None,4]
t1 = make_tree(ex1)
t2 = make_tree(ex2)
sol1 = test.isBalanced(t1)
sol2 = test.isBalanced(t2)

print(sol1)
print(sol2)
print(test.isBalanced(TreeNode(None)))