# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Doesn't work because leaf nodes aren't actually set to None, no idea why
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def successor(root: TreeNode) -> int:
            root = root.right
            while root.left:
                root = root.left
            
            val = root.val
            root = None
            return val

        def predecessor(root: TreeNode) -> int:
            root = root.left
            while root.right:
                root = root.right
            
            val = root.val
            root = None
            return val
            
        node = root
        found = False

        while node:
            if node.val > key:
                node = node.left
            elif node.val < key:
                node = node.right
            else:
                found = True
                break
        
        if not found:
            return root
        
        if not node.left and not node.right:
            node = None
        elif node.right:
            node.val = successor(node)
        elif node.left:
            node.val = predecessor(node)
        
        return root
            
# Recursive calls that end up rebalancing the tree. 
class workingSolution:
    # One step right and then always left
    def successor(self, root: TreeNode) -> int:
            root = root.right
            while root.left:
                root = root.left
            return root.val
        
    # One step left and then always right
    def predecessor(self, root: TreeNode) -> int:
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # The node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root

            


