# https://leetcode.com/problems/reverse-nodes-in-k-group?envType=problem-list-v2&envId=2wycmzu3

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(n)
    # Space O(1)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(node: Optional[ListNode]) -> Optional[ListNode]:
            i = 0
            while node and i < k:
                node = node.next
                i += 1
            return node

        dummy = ListNode(0, head)
        startNode = dummy
        kNode = getKth(startNode)
        while kNode:
            previousNode = kNode.next
            currentNode = startNode.next

            while previousNode != kNode:
                temp = currentNode.next
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = temp

            temp = startNode.next
            startNode.next = kNode
            startNode = temp
            kNode = getKth(startNode)

        return dummy.next
