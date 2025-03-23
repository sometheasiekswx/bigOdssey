from math import inf

"""
Brute force:
- 2 loops to calculate every subarray sum
- Find subarray sum of all the window sizes from from 1 to n
- Time complexity: O(n^2)

Two pointers:
- Start left and right pointer at 0, window size is 1
- Total starts at initial number at index 0
- If total >= target:
    - Update minimum size
    - Increase left pointer by 1
    - Minus old left pointer value
    - This decreases window size by 1, we want to find the smallest window
- If total < target:
    - Increase right pointer by 1
    - Add new value on new right index
    - This increases window size by 1, we need to find a new valid window
- If right pointer goes out of bounds, we explored all subarrays
"""

class Solution:
    # Time: O(n)
    # Space: O(1)
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        total, result = nums[0], inf
        while right < n:
            if total >= target:
                result = min(result, right-left + 1)
                total -= nums[left]
                left += 1
                continue
            right += 1
            if right < n: total += nums[right]

        return int(result) if result != inf else 0
