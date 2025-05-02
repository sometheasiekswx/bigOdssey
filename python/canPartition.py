# https://leetcode.com/problems/partition-equal-subset-sum/?envType=problem-list-v2&envId=2wyykuvs

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        remains = set()
        for num in nums:
            if num in remains:
                return True
            newRemains = set()
            for remain in remains:
                newRemains.add(remain-num)
            remains = remains.union(newRemains)

            remain = half - num
            if remain == 0:
                return True
            remains.add(remain)

        return False
