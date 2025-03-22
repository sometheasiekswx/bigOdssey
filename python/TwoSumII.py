# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    # Time: O(n)
    # Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target: return [left + 1, right + 1]
            elif total < target: left += 1
            elif total > target: right -= 1
