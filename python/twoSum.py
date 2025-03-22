# https://leetcode.com/problems/two-sum/

class Solution:
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        remains = {}
        for i, num in enumerate(nums):
            if num in remains:
                return [i, remains[num]]
            remain = target - num
            remains[remain] = i
