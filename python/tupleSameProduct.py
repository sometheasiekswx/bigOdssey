# https://leetcode.com/problems/tuple-with-same-product

# Calculate product of every unique pairs
# Count occurence of each product
# Products with counts >= 2 can form (4 * count) * (count - 1) tuples

from typing import List
from collections import defaultdict

class Solution:
    # Time: O(n)
    # Space: O(n)
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        productsCounts = defaultdict(lambda: 0)
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                productsCounts[product] += 1

        result = 0
        for product, count in productsCounts.items():
            if count >= 2:
                result += (4 * count) * (count - 1)
        return result
