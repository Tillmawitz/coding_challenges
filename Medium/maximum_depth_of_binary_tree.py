# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Queue beat 32% runtime and 22% memory
from collections import deque

class qSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif root.left == None and root.right == None:
            return 1

        q = deque()
        # Trying to make a tuple in one line
        q.append((root, 1))
        max_depth = 0

        while len(q) > 0:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        
        return max_depth

# Whereas the list approach beats 100% runtime and 99.91% in memory. Since we need to check the depth of all branches, we have to follow all possible branches so dfs vs. bfs doesn't matter. While complexity in terms of time is the same, lists are less complicated and faster than queues which are essentially doubly linked lists. Time complexity is log(n) and memory is n.
class listSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif root.left == None and root.right == None:
            return 1

        l = []
        # Trying to make a tuple in one line
        l.append((root, 1))
        max_depth = 0

        while len(l) > 0:
            node, depth = l.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                l.append((node.left, depth + 1))
            if node.right:
                l.append((node.right, depth + 1))
        
        return max_depth

# Cleaner solution
class cleanSolution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth