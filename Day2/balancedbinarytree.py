from queue import Queue

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.val} - {self.left}, {self.right})"


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
    """
    This implementation is very naive and breaks for complicated examples.
    """
    try:
        root = TreeNode(nums[0])
    except IndexError:
        return TreeNode(None)
    nums = nums[1:]
    i = 0
    q = Queue()
    q.put(root)
    while i < len(nums) - 1:
        cur = q.get()
        l = TreeNode(nums[i]) if nums[i] != None else None
        r = TreeNode(nums[i + 1]) if nums[i + 1] != None else None
        cur.left = l
        cur.right = r
        i += 2
        q.put(l)
        q.put(r)
    return root


test = Solution()

ex1 = [3, 9, 20, None, None, 15, 7]
ex2 = [1, 2, 2, 3, 3, None, None, 4, 4]
ex3 = []

# this tree breaks my naive make_tree function implementation
# eventually I will fix the function when I have time so that
# any tree can be tested. After the fixes are implemented, this
# should return False.
ex4 = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]


t1 = make_tree(ex1)
t2 = make_tree(ex2)
t3 = make_tree(ex3)
# t4 = make_tree(t4)
sol1 = test.isBalanced(t1)
sol2 = test.isBalanced(t2)
sol3 = test.isBalanced(t3)
# sol4 = test.isBalanced(t4)

print(sol1)
print(sol2)
print(sol3)
# print(sol4)
