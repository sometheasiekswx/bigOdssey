# https://leetcode.com/problems/combination-sum
'''
Backtrack:
- Take current candidate, check same candidate
- Take nothing, check next candidate
'''

from typing import List

class Solution:
    # Time: O(2^n)
    # Space: O(2^n)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        def backtrack(i: int, combination: list[int], total: int) -> None:
            if total == target:
                result.append(combination)
                return

            if total > target: return
            if i == n: return

            backtrack(i, combination + [candidates[i]], total + candidates[i])
            backtrack(i+1, combination, total)
        backtrack(0, [], 0)
        return result
