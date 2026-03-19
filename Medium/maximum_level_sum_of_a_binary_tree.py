# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
# Pretty fast solution, does what it says on the tin. For each iteration of the while loop we are processing a single level and adding the next level to the queue, with the for loop allowing us to process a single level at a time.
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        max_sum = [float('-inf'), 0]
        level = 1

        while q:
            level_len = len(q)
            level_sum = 0

            for i in range(level_len):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if level_sum > max_sum[0]:
                max_sum = [level_sum, level]
            
            level += 1
        
        return max_sum[1]