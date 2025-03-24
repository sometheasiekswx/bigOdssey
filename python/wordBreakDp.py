# Link: https://leetcode.com/problems/word-break-ii

"""
Iterate backward through s, finding and storing valid words
    - If valid word ends at last letter of s, store it directly
    - If the valid word doesn't end with last leter of s
        - Check if it can combine with previously stored words that ended with last letter of s
    - Store all possible sentences at each index
"""

class Solution:
    # Time: O(n*2^n)
    # Space: O(2^n)
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        n, wordDictUnique = len(s), set(wordDict)
        dp = {n:[]}
        for startIndex in range(n - 1, -1, -1):
            validWords, currentWord = [], ""
            for endIndex in range(startIndex, n):
                currentWord += s[endIndex]
                if currentWord not in wordDictUnique:
                    continue
                if endIndex == n - 1:
                    validWords.append(currentWord)
                    continue
                previousWords = dp.get(endIndex + 1)
                if not previousWords:
                    continue
                for previousWord in previousWords:
                    validWords.append(currentWord + " " + previousWord)
            dp[startIndex] = validWords
        return dp[0]
