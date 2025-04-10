# https://leetcode.com/problems/coin-change-ii

from typing import List

class Solution:
    # Time: O(n*amount)
    # Space: O(amount)
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0]*amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        return dp[-1]

    # Time: O(n*amount)
    # Space: O(amount)
    def changeBottomUpOptimizedSpaceInitial(self, amount: int, coins: List[int]) -> int:
        previous = [1] + [0]*amount
        for i in range(1, amount+1):
            remain = i - coins[0]
            if remain >= 0:
                previous[i] = previous[remain]

        current = previous.copy()
        for coin in coins[1:]:
            for i in range(amount+1):
                remain = i - coin
                numberOfWaysToMakeRemain = current[remain] if remain >= 0 else 0
                current[i] = previous[i] + numberOfWaysToMakeRemain
            previous = current

        return previous[-1]

    # Time: O(n*amount)
    # Space: O(n*amount)
    def changeBottomUp(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0]*n for _ in range(amount + 1)]
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, amount+1):
            for i, coin in enumerate(coins):
                previous = dp[i][i-1] if i > 0 else 0
                remain = i - coin
                current = dp[remain][i] if remain >= 0 else 0
                dp[i][i] = previous + current

        return dp[amount][-1]

    # Time: O(n^amount)
    # Space: O(n^amount)
    def changeBacktrackMemo(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        memoCache = {}
        def numberOfWays(i, total):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if i == n:
                return 0

            if (i, total) in memoCache:
                return memoCache[(i, total)]
            waysIftake = numberOfWays(i, total + coins[i])
            waysIfskip = numberOfWays(i+1, total)
            totalWays = waysIftake + waysIfskip
            memoCache[(i, total)] = totalWays
            return totalWays

        return numberOfWays(0,0)
