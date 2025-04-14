from heapq import heappush, heappop
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
- Collect all node values into nodesValues
    - Go through every ListNode in lists
    - For each ListNode, heappush the values of all its node
- Create new ListNode from nodesValues
    - Start with a dummy node
    - Heappop from nodesValues and attach it to current node
    - Shift current to the next node
"""
class Solution:
    # Time: O(nlogn)
    # Space: O(n)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodesVals = []
        for listNode in lists:
            current = listNode
            while current:
                heappush(nodesVals, current.val)
                current = current.next

        merged = ListNode(0)
        current = merged
        while nodesVals:
            val = heappop(nodesVals)
            current.next = ListNode(val)
            current = current.next
        return merged.next

    # Time: O(nlogn)
    # Space: O(n)
    def mergeKListsInitial(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodesVals = []
        while lists:
            updated = False
            for i, l in enumerate(lists):
                if not l:
                    continue
                heappush(nodesVals, l.val)
                updated = True

                if not l.next:
                    del lists[i]
                    continue
                lists[i] = l.next
            if not updated:
                break
        merged = ListNode(0, None)
        current = merged
        while nodesVals:
            val = heappop(nodesVals)
            current.next = ListNode(val, None)
            current = current.next
        return merged.next

    def convertListToListNode(self, l: List[int]) -> Optional[ListNode]:
        node = ListNode(0)
        current = node
        for val in l:
            current.next = ListNode(val, None)
            current = current.next
        return node.next

    def convertNumberListsListToListNodeList(self, lists: List[List[int]]) -> List[Optional[ListNode]]:
        result = []
        for l in lists:
            result.append(self.convertListToListNode(l))
        return result

    def printListNode(self, node: Optional[ListNode]) -> None:
        current = node
        while current:
            if not current.next:
                print(current.val, end=' -> None\n')
                break
            print(current.val, end=' -> ')
            current = current.next


if __name__ == "__main__":
    solution = Solution()
    tests = [
        [[1,4,5],[1,3,4],[2,6]],
        [[1,4,5],[1,3,4],[2,6],[],[1],[5,5,5,5,5]],
    ]
    for test in tests:
        lists = solution.convertNumberListsListToListNodeList(test)
        solution.printListNode(solution.mergeKLists(lists))
