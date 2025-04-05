# https://leetcode.com/problems/maximum-number-of-robots-within-budget

from collections import deque
from typing import List

'''
Use sliding window to check consecutive robots
    - Increase window size if <= budget
    - Decrease window size if > budget
Use monotonic decreasing stack to keep track of charge times
    - Keep highest number at the bottom
    - Keep lowest number at the top
'''
class Solution:
    # Time: O(n)
    # Space: O(n)
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        result = leftI = rightI = 0
        currentChargeTimes = deque([chargeTimes[rightI]])
        sumRunningCost = runningCosts[rightI]
        while rightI < n:
            k = rightI - leftI + 1
            total = currentChargeTimes[0] + (k * sumRunningCost)
            if total <= budget:
                result = max(result, k)

            if total <= budget or leftI >= rightI:
                rightI += 1
                if rightI >= n:
                    break
                sumRunningCost += runningCosts[rightI]
                while currentChargeTimes and chargeTimes[rightI] > currentChargeTimes[-1]:
                    currentChargeTimes.pop()
                currentChargeTimes.append(chargeTimes[rightI])
                continue

            sumRunningCost -= runningCosts[leftI]
            if currentChargeTimes and chargeTimes[leftI] == currentChargeTimes[0]:
                currentChargeTimes.popleft()
            leftI += 1

        return result
