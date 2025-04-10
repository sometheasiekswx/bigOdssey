# https://leetcode.com/problems/target-sum/?envType=problem-list-v2
# https://docs.google.com/document/d/1C0zy8ryjhXsJnVS5gwfvH3G4Uv0cOamenWcMSVp5VpQ/edit?usp=sharing

from collections import defaultdict
from typing import List

class Solution:
    # totalSum = sum(nums)
    # Backtrack with memo:
    #  - Time: n * totalSum
    #  - Space: n * totalSum

    # DP Space Optimized:
    #  - Time: n * totalSum
    #  - Space: totalSum
    '''
    Find the new sum after adding and subtracting the nums one by one
    Keep track of the count of previous sum
    Add and minus previous sum using the next num to get new sum
    Use count of previous in new sum
       -5 -4 -3 -2 -1  0 +1 +2 +3 +4 +5
                       1
    1               1     1
    1            1     2     1
    1         1     3     3     1
    1      1     4     6     4     1
    1  1      5     10    10   [5]     1
    '''
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        memo = {}
        def backtrack(i, currentSum, result) -> int:
            if (i, currentSum) in memo:
                return memo[i, currentSum]
            if i == n and currentSum == target:
                return result + 1
            if i == n:
                return 0

            add = backtrack(i + 1, currentSum + nums[i], result)
            memo[i + 1, currentSum + nums[i]] = add
            minus = backtrack(i + 1, currentSum - nums[i], result)
            memo[i + 1, currentSum - nums[i]] = minus
            return add + minus
        # return backtrack(0,0,0)

        # DP Solution
        sumsCounts = defaultdict(lambda: 0)
        sumsCounts[0] = 1
        for i, num in enumerate(nums):
            newSumsCounts = defaultdict(lambda: 0)
            for currentSum, count in sumsCounts.items():
                newSumsCounts[currentSum+num] += count
                newSumsCounts[currentSum-num] += count
            sumsCounts = newSumsCounts
        return sumsCounts[target]
