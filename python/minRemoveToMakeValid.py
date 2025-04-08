# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    # Time: O(n)
    # Space: O(n)
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        brackets = 0
        for letter in s:
            if letter not in ['(', ')']:
                result.append(letter)
            elif letter == '(':
                brackets += 1
                result.append(letter)
            elif letter == ')' and brackets > 0:
                brackets -= 1
                result.append(letter)
        i = len(result) - 1
        while brackets > 0 and i >= 0:
            if result[i] == '(':
                del result[i]
                brackets -= 1
            i -= 1
        return ''.join(result)
