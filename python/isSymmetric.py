# https://leetcode.com/problems/symmetric-tree/

from collections import deque
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        nodes = deque([(root.left, root.right)])
        while nodes:
            leftNode, rightNode = nodes.popleft()

            if not leftNode and not rightNode:
                continue

            if not leftNode or not rightNode:
                return False

            if leftNode.val == rightNode.val:
                nodes.append((leftNode.left, rightNode.right))
                nodes.append((leftNode.right, rightNode.left))
                continue

            if leftNode.val != rightNode.val:
                return False

        return True
