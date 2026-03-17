"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

    Choose any node in the binary tree and a direction (right or left).
    If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
    Change the direction from right to left or from left to right.
    Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:

Input: root = [1]
Output: 0

Constraints:

    The number of nodes in the tree is in the range [1, 5 * 104].
    1 <= Node.val <= 100

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solidly middle of the pack in both memory and time. Depending on the direction we came into the node, we want to return the length of the zigzag from that side. Really need to try starting simple, I keep pre-optimizing and getting wrong solutions.
class recursiveSolution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zigzag(node: Optional[TreeNode], zig_or_zag: str) -> int:
            nonlocal longest_path
            if not node:
                return 0

            r_path = 1 if node.right else 0
            l_path = 1 if node.left else 0
            
            r_path = r_path + zigzag(node.right, 'r')
            l_path = l_path + zigzag(node.left, 'l')

            longest_path = max(longest_path, r_path, l_path)

            if zig_or_zag == 'r':
                return l_path
            elif zig_or_zag == 'l':
                return r_path

        longest_path = 0
        zigzag(root, 's')
        return longest_path

class cleanerSolution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.pathLength = 0
        
        def dfs(node, goLeft, steps):
            if node:
                self.pathLength = max(self.pathLength, steps)
                if goLeft:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)
        
        dfs(root, True, 0)
        return self.pathLength