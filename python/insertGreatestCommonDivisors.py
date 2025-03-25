# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

from math import gcd
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time: O(n)
    # Space: O(1)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousNode = head
        currentNode = head.next
        while currentNode:
            gcdNode = ListNode(
                gcd(previousNode.val, currentNode.val), next=currentNode
            )
            previousNode.next = gcdNode
            previousNode = currentNode
            currentNode = currentNode.next

        return head
