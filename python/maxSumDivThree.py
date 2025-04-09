# https://leetcode.com/problems/greatest-sum-divisible-by-three

class Solution:
    # Time: O(n)
    # Space: O(1)
    def maxSumDivThreeOptimized(self, nums: list[int]) -> int:
        divisor = 3
        remains = [0] * divisor
        for num in nums:
            tempRemains = remains.copy()
            for i in range(divisor):
                if remains[i] <= 0 and i != 0:
                    continue
                remain = (i + num) % 3
                tempRemains[remain] = max(tempRemains[remain], remains[i] + num)
            remains = tempRemains
        return remains[0]

    # Time: O(n)
    # Space: O(1)
    def maxSumDivThree(self, nums: list[int]) -> int:
        remain0 = remain1 = remain2 = 0
        divisor = 3
        for num in nums:
            remain0Temp = remain1Temp = remain2Temp = 0
            remains = num % divisor
            if remains == 0:
                remain0Temp = remain0 + num if remain0 > 0 else max(num, remain0)
                remain1Temp = remain1 + num if remain1 > 0 else remain1
                remain2Temp = remain2 + num if remain2 > 0 else remain2
            elif remains == 1:
                remain1Temp = (
                    max(remain1, remain0 + num) if remain0 > 0 else max(remain1, num)
                )
                remain0Temp = (
                    max(remain0, remain2 + num) if remain2 > 0 else remain0
                )
                remain2Temp = (
                    max(remain2, remain1 + num) if remain1 > 0 else remain2
                )
            elif remains == 2:
                remain2Temp = (
                    max(remain2, remain0 + num) if remain0 > 0 else max(remain2, num)
                )
                remain1Temp = (
                    max(remain1, remain2 + num) if remain2 > 0 else remain1
                )
                remain0Temp = (
                    max(remain0, remain1 + num) if remain1 > 0 else remain0
                )
            remain1, remain0, remain2 = remain1Temp, remain0Temp, remain2Temp
        return remain0
