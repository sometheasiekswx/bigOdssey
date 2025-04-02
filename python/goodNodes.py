# https://leetcode.com/problems/count-good-nodes-in-binary-tree

from math import inf
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
- Start from -infinity as the previous max value
- Start from root

- Check if node value is greater than previous max
- Add new left and right nodes to compare
- Update new previous max value

[-inf]
[3]

[3]
[[1,4]]

[1,4]
[[3], [1,5]]
'''
class Solution:
    # Time: O(n)
    # Space: O(n)
    def goodNodes(self, root: TreeNode) -> int:
        goodCount = 0
        nodes = deque([(-inf,[root])])
        while nodes:
            previousVal, currentNodes = nodes.popleft()
            for _ in range(len(currentNodes)):
                currentNode = currentNodes.pop()
                if currentNode.val >= previousVal:
                    goodCount += 1
                temp = []
                if currentNode.left:
                    temp.append(currentNode.left)
                if currentNode.right:
                    temp.append(currentNode.right)
                if temp:
                    nodes.append((max(currentNode.val,previousVal), temp))
        return goodCount
