# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

class Solution:
    def bisectRight(self, nums: list[int], target: int, left: int = 0, right: int = None) -> int:
        if right is None:
            right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid
            else:
                left = mid + 1

        return left

    def bisectLeft(self, nums: list[int], target: int, left: int = 0, right: int = None) -> int:
        if right is None:
            right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1

        return left

    def maximumCount(self, nums: list[int]) -> int:
        n = len(nums)
        midleft = self.bisectLeft(nums, 0)
        midRight = self.bisectRight(nums, 0)
        return max(midleft, n-midRight)
