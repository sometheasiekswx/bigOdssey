# https://leetcode.com/problems/summary-ranges

from typing import List

class Solution:
    # Time: O(n)
    # Space: O(n)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n < 1:
            return []
        start = nums[0]
        intervals = []
        for i in range(1, n):
            if nums[i] - 1 == nums[i - 1]:
                continue
            intervals.append(f'{start}')
            if start != nums[i - 1]:
                intervals[-1] += f'->{nums[i - 1]}'
            start = nums[i]
        intervals.append(f'{start}')
        if start != nums[-1]:
            intervals[-1] += f'->{nums[-1]}'
        return intervals
