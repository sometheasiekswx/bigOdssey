# https://leetcode.com/problems/coin-change

# Find number of ways to make 0, which is 0
# Find number of ways to make 1, 2, 3, ..., amount
# Ways to make i is taking all the coins less
# than i and calculating 1 + ways to make (i - coin taken)

# [1,2,5] amount = 4
# 0: 0 coins
# 1: 1 coins + {1-1} ways = 1 coins + 0 = 1 coins
# 2: min() -> 1
#   - 1 coins + {2-2} = 1 coins
#   - 1 coins + {2-1} = 1 coins + {1} = 1 + 1 = 2 coins
# 3: -> 2
#   - 1 coins + {3-2} = 1 coins + {1} = 1 + 1 = 2 coins
#   - 1 coins + {3-1} = 1 coins + {2} = 1 + 1 = 2 coins
# 4: min() -> 2
#   - 1 coins + {4-2} = 2
#   - 1 coins + {4-1} = 1 coins + {3} = 1 + 2 = 3

import math

class Solution:
    # n = len(coins)
    # m = len(amount)
    # Time: O(n*m)
    # Space: O(m)
    def coinChange(self, coins: list[int], amount: int) -> int:
        minWaysToMake = [math.inf] * (amount + 1)
        minWaysToMake[0] = 0
        coins.sort()

        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i: break
                ways = 1 + minWaysToMake[i - coin]
                minWaysToMake[i] = min(ways, minWaysToMake[i])

        return int(minWaysToMake[amount]) if minWaysToMake[amount] != math.inf else -1
