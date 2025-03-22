# https://leetcode.com/problems/valid-palindrome/

class Solution:
    # Time: O(n)
    # Space: O(n)
    def isPalindrome(self, s: str) -> bool:
        letters = [letter.lower() for letter in s if letter.isalpha() or letter.isnumeric()]
        left, right = 0, len(letters) - 1
        while left < right:
            if letters[left] != letters[right]: return False
            left += 1
            right -= 1
        return True
