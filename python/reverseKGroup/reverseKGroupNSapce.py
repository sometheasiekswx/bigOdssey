# https://leetcode.com/problems/reverse-nodes-in-k-group?envType=problem-list-v2&envId=2wycmzu3

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time: O(n)
    # Space: O(n)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ks, nonKs, nonKsTemp = [], [], []
        current = head
        i = 1
        while current:
            if i % k == 0:
                ks.append(current)
                nonKs.append(nonKsTemp)
                nonKsTemp = []
            else:
                nonKsTemp.append(current)

            current = current.next
            if current is None and nonKsTemp:
                nonKs.append(nonKsTemp)
            i += 1

        dummy = ListNode()
        current = dummy

        for i in range(len(ks)):
            current.next = ks[i]
            current = current.next
            for j in range(len(nonKs[i])-1,-1,-1):
                current.next = nonKs[i][j]
                current = current.next

            if i != len(ks) - 1:
                continue

            if i == len(nonKs) - 1:
                current.next = None
                continue

            for j in range(len(nonKs[i+1])):
                current.next = nonKs[i+1][j]
                current = current.next

        return dummy.next
