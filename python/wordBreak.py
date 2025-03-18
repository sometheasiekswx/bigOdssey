# Link: https://leetcode.com/problems/word-break-ii

# Iterate through characters of s starting at index 0
# Add new letters to form current word
# If current word is in wordDict:
#   - Branch out to explore that path
#   - Add current word to valid words list
#   - Reset current word to ""
# If end of s is reached and if current word is "", we have a valid list
# If end of s is reached and current word is not "", we don't have a valid list
class Solution:
    # Time: O(2^n)
    # Space: O(2^n)
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        n = len(s)
        result = []

        def backtrack(i: int, current: str, valid: list[str]) -> None:
            if i == n and current == "":
                result.append(" ".join(valid))
                return
            if i == n:
                return

            current += s[i]
            if current in wordDict:
                backtrack(i+1, "", valid + [current])
            backtrack(i+1, current, valid)

        backtrack(0,"", [])

        return result
