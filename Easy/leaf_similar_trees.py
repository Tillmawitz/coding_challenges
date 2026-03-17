"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:

    The number of nodes in each tree will be in the range [1, 200].
    Both of the given trees will have values in the range [0, 200].
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Straightforward dfs, when you reach a leaf add it to the list then check if the lists are the same. Could hypothetically save some memory by not storing the leaves of the second tree and instead comparing the leaves values directly to the leaf list of the first tree. Could further optimize memory by traversing tree1 until the first leaf, then traverse tree2 and directly comparing values.
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # If one is empty, return true if both are empty
        if not root1 or not root2:
            return not root1 and not root2

        def dfs(root: Optional[TreeNode]) -> list[int]:
            stack = [root]
            leaves = []

            while len(stack) > 0:
                node = stack.pop()

                if not node.right and not node.left:
                    leaves.append(node.val)
                    continue
                
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            return leaves

        leaves1 = dfs(root1)
        leaves2 = dfs(root2)
        
        return leaves1 == leaves2

# Due to the recursive calls this doesn't change the memory complexity in Python, but in some languages you can write in such a way that the recursion uses constant memory. Also this doesn't meet the criteria for the question as designed, just a provided alternative.
class recursiveSolution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))