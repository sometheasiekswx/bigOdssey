# https://leetcode.com/problems/house-robber

from collections import deque

class Solution:
    # Time: O(n)
    # Space: O(1)
    def rob(self, nums: list[int]) -> int:
        #       [2, 7, 9,  3,  1]
        # [0, 0, 2, 7, 11, 11, 12]
        moneyRobbed = deque([0,0])
        for i, num in enumerate(nums):
            takeAdjancent = moneyRobbed[-1]
            takeSkipOne = moneyRobbed[-2] + num
            moneyRobbed.append(max(takeAdjancent, takeSkipOne))
            moneyRobbed.popleft()
        return moneyRobbed[-1]
