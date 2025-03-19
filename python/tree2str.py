from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(n)
    # Space: O(n)
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def node2str(node: Optional[TreeNode]) -> str:
            if not node:
                return ""
            if node.left and node.right:
                return f"({node.val}{node2str(node.left)}{node2str(node.right)})"
            if node.left:
                return f"({node.val}{node2str(node.left)})"
            if node.right:
                return f"({node.val}(){node2str(node.right)})"
            return f"({node.val})"

        return node2str(root)[1:-1]
