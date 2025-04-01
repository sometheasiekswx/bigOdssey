from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # m = len(head)
    # Time: O(m) <- O(2m)
    # Space: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeCount = 0
        current = head
        while current:
            nodeCount += 1
            current = current.next

        if nodeCount < 2: return None
        if n >= nodeCount: return head.next
        indexToRemove = nodeCount - n
        previous = head
        current = head.next.next
        i = indexToRemove - 1
        while i > 0:
            previous = previous.next
            current = current.next
            i -= 1
        previous.next = current
        return head

    # m = len(head)
    # Time: O(m)
    # Space: O(m)
    def removeNthFromEndLinearSpace(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       nodes = []
       current = head
       while current:
           nodes.append(current)
           current = current.next

       if len(nodes) < 2: return None
       if n >= len(nodes): return head.next if head and head.next else None
       nodes[-n-1].next = None if n == 1 else nodes[-n+1]
       return head
