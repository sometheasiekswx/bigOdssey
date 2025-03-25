# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    # Time: O(n)
    # Space: O(n)
    def myAtoi(self, s: str) -> int:
        digits = s.strip()
        n = len(digits)
        if n == 0: return 0

        negative = False
        if digits[0] == "-":
            negative = True
            digits = digits[1:]
            n -= 1
        elif digits[0] == "+":
            digits = digits[1:]
            n -= 1

        validNumbers = ""
        for i in range(n):
            if not digits[i].isdigit(): break
            validNumbers += digits[i]

        while validNumbers and validNumbers[0] == "0":
            validNumbers = validNumbers[1:]

        total, count = 0, len(validNumbers)
        for i in range(count):
            total += int(validNumbers[i]) * 10 **(count - i - 1)

        total = -total if negative else total
        lowerLimit, upperLimit = -(2**31), 2**31 - 1
        if total < lowerLimit: total = lowerLimit
        elif total > upperLimit: total = upperLimit

        return total
