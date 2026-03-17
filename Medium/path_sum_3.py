"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:

    The number of nodes in the tree is in the range [0, 1000].
    -10^9 <= Node.val <= 10^9
    -1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Took a while as I tried to pre-optimize by excluding nodes and sums that exceed the target, which was objectively wrong as node values can be negative. This solution was slow, beating only 29% and running in 133 ms while most ran in like 3 ms. Much more memory efficient though, using less memory than 99.37% of solutions
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        # Using tuples to keep track of sums along path because python would allow nodes to modify other node's lists
        stack = [(root, ())]
        paths = 0

        while stack:
            node, sums = stack.pop()
            new_sums = []

            if node.val == targetSum:
                paths += 1
            
            for s in sums:
                path_sum = s + node.val
                if path_sum == targetSum:
                    paths += 1
                    
                # Need to append all path sums as node vals can be negative
                new_sums.append(path_sum)
            
            new_sums.append(node.val)

            new_tup = tuple(new_sums)
            if node.right:
                stack.append((node.right, new_tup))
            
            if node.left:
                stack.append((node.left, new_tup))

        return  paths

# This solution uses the idea of hashed prefix sums instead of iterating through a list of all the previous sums, and obvious improvement on my solution. If implementing iteratively you need to make use of an immutabledict or similar like in the above solution, which is not part of the default collections.
class betterSolution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node:
                return 
            
            # The current prefix sum
            curr_sum += node.val
            
            # Here is the sum we're looking for
            if curr_sum == k:
                count += 1
            
            # The number of times the curr_sum − k has occurred already, 
            # determines the number of times a path with sum k 
            # has occurred up to the current node
            count += h[curr_sum - k]
            
            # Add the current sum into a hashmap
            # to use it during the child nodes' processing
            h[curr_sum] += 1
            
            # Process the left subtree
            preorder(node.left, curr_sum)
            # Process the right subtree
            preorder(node.right, curr_sum)
            
            # Remove the current sum from the hashmap
            # in order not to use it during 
            # the parallel subtree processing
            h[curr_sum] -= 1
            
        count, k = 0, sum
        h = defaultdict(int)
        preorder(root, 0)
        return count