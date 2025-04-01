# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    # Time: O(n)
    # Space: O(n)
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        previous = nums[0]
        repeatCount, indexesToRemove = 0, []
        for i in range(1, n):
            num = nums[i]
            if num == previous: repeatCount += 1
            elif num != previous:
                previous = num
                repeatCount = 0

            if repeatCount > 1: indexesToRemove.append(i)

        for i in reversed(indexesToRemove): del nums[i]

        return len(nums)
