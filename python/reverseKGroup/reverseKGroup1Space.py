# https://leetcode.com/problems/reverse-nodes-in-k-group?envType=problem-list-v2&envId=2wycmzu3

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time: O(n)
    # Space: O(1)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # TODO: Complete the code on my own
        return dummy.next
