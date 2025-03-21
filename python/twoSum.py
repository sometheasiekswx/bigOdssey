class Solution:
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remains = {}
        for i, num in enumerate(nums):
            if num in remains:
                return [i, remains[num]]
            remain = target - num
            remains[remain] = i
